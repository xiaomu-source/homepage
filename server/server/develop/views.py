import inflection
from rest_framework.decorators import action

from develop.models import Code
from develop.serializers import CodeSerializer
from utils.authentications import AccountViewSet
from utils.decorator import schema_required
from utils.response import APIResponse, BadResponse
from utils.utils import filter_queryset_by_partial_match, get_list_view_data
from utils.validations import StrField, CommaListField


class CodeViewSet(AccountViewSet):

    @schema_required(with_list=True)
    @action(methods=["post"], detail=False, url_path="get-list")
    def get_list(self, request):
        try:
            return APIResponse(get_list_view_data(Code, CodeSerializer, self.validated_data))
        except Exception as e:
            return BadResponse(str(e))

    @schema_required(
        name = StrField(required=False, help_text="文件名称"),
        type = StrField(required=False, help_text="文件类型"),
        url = StrField(required=False, help_text="下载地址"),
        remark = StrField(required=False, help_text="备注"),
    )
    @action(methods=["post"], detail=False, url_path="create-code")
    def create_code(self, request):
        try:
            data = {inflection.underscore(key): value for key, value in self.validated_data.items() if value}
            code = Code.objects.create(**data)
            return APIResponse(data=CodeSerializer(code).data, message="操作成功")
        except Exception as e:
            return APIResponse(str(e))

    @schema_required(
        with_id=True,
        name=StrField(required=False, help_text="文件名称"),
    )
    @action(methods=["post"], detail=False, url_path="delete-code")
    def delete_code(self, request):
        try:
            code_info = Code.objects.get(id=self.validated_data.get("id"))
            code_info.delete()
            return APIResponse(message='File deleted successfully')
        except Code.DoesNotExist:
            return BadResponse("Code info not found")
        except Exception as e:
            return BadResponse(str(e))

    @schema_required(
        ids=CommaListField(required=False, help_text="文件名称"),
    )
    @action(methods=["post"], detail=False, url_path="delete-all")
    def delete_all(self, request):
        return APIResponse()

    @action(methods=["post"], detail=False, url_path="singleCurdFrontAndBack")
    def single_curd_front_and_back(self, request):
        return APIResponse()

    @action(methods=["post"], detail=False, url_path="download")
    def download(self, request):
        return APIResponse()

    @action(methods=["post"], detail=False, url_path="collections")
    def collections(self, request):
        return APIResponse()


class ModelViewSet(AccountViewSet):

    @action(methods=["post"], detail=False, url_path="get-list")
    def get_list(self, request):
        return APIResponse()

