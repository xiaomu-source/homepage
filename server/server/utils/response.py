from datetime import datetime

from rest_framework.response import Response
from rest_framework import status as http_status

class APIResponse(Response):
    def __init__(self, data=None, message:str="Success.", status=http_status.HTTP_200_OK, template_name=None, headers=None, exception=False, content_type=None):
        data = {
            "data": data,
            "message": message,
            "status": 1,
            "time": int(datetime.timestamp(datetime.now()))
        }
        super().__init__(data=data, status=status, template_name=template_name, headers=headers, exception=exception, content_type=content_type)

class BadResponse(Response):
    def __init__(self, data=None, message: str="Fail.", status=http_status.HTTP_400_BAD_REQUEST, template_name=None, headers=None, exception=False,
                 content_type=None):
        data = {
            "error": data,
            "message": message,
            "status": 0,
            "time": int(datetime.timestamp(datetime.now()))
        }
        super().__init__(data=data, status=status, template_name=template_name, headers=headers, exception=exception,
                         content_type=content_type)