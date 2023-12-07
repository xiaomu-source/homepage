import base64
import json

import jwt
from django.db.models import QuerySet
from rest_framework.authentication import BaseAuthentication, get_authorization_header, SessionAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.viewsets import ViewSet as _ViewSet

from server.settings.base import SIGN_KEY
from system.models import Account
from utils.utils import slice_array


def padding_base64(value: str) -> str:
    num = len(value) % 4
    num = 4 - num if num else 0
    return value + "=" * num
def get_account_by_jwt_token(jwt_token):
    jwt_data = jwt_token.strip().split(".")
    if len(jwt_data) != 3:
        raise AuthenticationFailed("JWT Authorization Data Error")
    # 检查 JWT Token 的正确性
    try:
        try:
            payload = base64.b64decode(padding_base64(jwt_data[1]))
            payload = json.loads(payload.decode())
        except Exception as e:
            raise AuthenticationFailed(f"Authorization payload decode failed, sign in again: {e}")
        account_id = payload["_id"]
        if not account_id:
            raise AuthenticationFailed("Authorization check account id failed")
        account: Account = Account.objects.get(id=account_id)
        try:
            jwt.decode(jwt_token, SIGN_KEY, algorithms=["HS256"])
        except Exception as e:
            raise AuthenticationFailed(f"Authorization check jwt failed, sign in again: {e}")
    except AuthenticationFailed as e:  # 明确鉴权错误，返回鉴权错误
        raise e
    except Exception as e:  # 其他类型错误（数据库，缓存，代码逻辑等），兜底返回 APIException
        raise e
    return account


class AccountAuthentication(BaseAuthentication):
    def __init__(self):
        super().__init__()

    def authenticate(self, request):
        authorization_header: bytes = get_authorization_header(request)
        if not authorization_header:
            raise AuthenticationFailed("Missing Authorization Header")

        jwt_token: str = authorization_header.decode("utf-8").split(" ")[1]
        account = get_account_by_jwt_token(jwt_token)
        return account, None

    def authenticate_header(self, request):
        return f"CSRF Failed: {request.META.get('HTTP_AUTHORIZATION')})"


class CSRFExemptAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return None  # To not perform the csrf check previously happening


class ViewSet(_ViewSet):
    # 数据经过校验之后存储的字段
    validated_data = {}

    def slice_query(self, query: QuerySet | list):
        current = self.validated_data.get("current") or 1
        page_size = self.validated_data.get("page_size") or 15
        if current is None or page_size is None:
            raise Exception("offset is None or limit is None")
        offset = (current - 1) * page_size
        return slice_array(query, offset, page_size)


class AccountViewSet(ViewSet):
    authentication_classes = (AccountAuthentication,)


class CSRFExemptViewSet(ViewSet):
    authentication_classes = (CSRFExemptAuthentication,)