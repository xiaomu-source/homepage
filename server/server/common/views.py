import math
import mimetypes
import os

from django.conf import settings
from django.core.exceptions import BadRequest
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action

from system.models import Resource
from utils.authentications import AccountViewSet
from utils.files import format_file_size, get_media_url
from utils.response import APIResponse


class FileViewSet(AccountViewSet):
    @action(methods=["post"], detail=False, url_path="upload")
    def upload(self, request):
        try:
            uploaded_file = request.FILES.get('file')
            if not uploaded_file:
                return BadRequest("没有上传文件")
            file_size = uploaded_file.size
            file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
            # 保存之后名字可能会改变，重新获取一下
            filename = default_storage.save(file_path, ContentFile(uploaded_file.read()))
            file_type, encoding = mimetypes.guess_type(file_path)
            new_resources = {
                'src_name': filename,
                'src_size': format_file_size(file_size),
                'src_type': file_type,
                'preview_path': filename,
                'download_path': filename,
                'delete_path': filename,
                "user": request.user,
            }
            Resource.objects.create(**new_resources)
            data = {
                "filename": filename,
                "previewUrl": get_media_url(filename),
                "downloadUrl": get_media_url(filename),
                "deleteUrl": get_media_url(filename),
            }
            return APIResponse(data=data, message="上传成功")
        except Exception as e:
            return BadRequest(str(e))

# 提供三个不需要认证就可以下载|查看|删除文件的接口
@csrf_exempt
def download_file(request, filename):
    media_file_path = os.path.join(settings.MEDIA_ROOT, filename)
    file_type, encoding = mimetypes.guess_type(media_file_path)
    if not default_storage.exists(media_file_path):
        return HttpResponse("找不到该文件", status=400)
    response = StreamingHttpResponse(open(media_file_path, "rb"))
    response["Content-Type"] = file_type
    response["Content-Disposition"] = f"attachment;filename={filename}"
    return response

@csrf_exempt
def preview_file(request, filename):
    media_file_path = os.path.join(settings.MEDIA_ROOT, filename)
    file_type, encoding = mimetypes.guess_type(media_file_path)
    if not default_storage.exists(media_file_path):
        return HttpResponse("找不到该文件", status=400)
    response = StreamingHttpResponse(open(media_file_path, "rb"))
    response["Content-Type"] = file_type
    response["Content-Disposition"] = f"attachment;filename={filename}"
    return response

@csrf_exempt
def delete_file(request, filename):
    media_file_path = os.path.join(settings.MEDIA_ROOT, filename)
    if not default_storage.exists(media_file_path):
        return HttpResponse("找不到该文件", status=400)
    Resource.objects.filter(src_name=filename).delete()
    default_storage.delete(media_file_path)
    return HttpResponse("删除成功！")
