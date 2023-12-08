import math

from django.conf import settings


def format_file_size(bytes):
    if bytes == 0:
        return '0 Bytes'

    sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB']
    i = int(math.floor(math.log(bytes, 1024)))
    file_size = round(bytes / math.pow(1024, i), 2)
    return f"{file_size} {sizes[i]}"

def get_media_url(file_name: str) -> str:
    file_name = file_name.strip("/")
    media_url =  f"{settings.HOST}{settings.MEDIA_URL}{file_name}"
    if media_url.startswith("http"):
        return media_url
    return f"http://{media_url}"

def get_media_delete_url(file_name: str) -> str:
    file_name = file_name.strip("/")
    media_delete_url = f"{settings.HOST}/v1/common/delete/{file_name}/"
    if media_delete_url.startswith("http"):
        return media_delete_url
    return f"http://{media_delete_url}"

def get_filename_from_media_url(file_name: str) -> str:
    return file_name.lstrip(settings.HOST) if settings.HOST in file_name else file_name