import uuid

from rest_framework.test import APITestCase

from blog.models import BlogPost
from system.models import Account, Role
from utils.utils import get_jwt_token


class BaseTestCase(APITestCase):
    def setUp(self) -> None:
        self.account = self.init_account()
        self.create_post(self.account)

    @classmethod


    def set_account_token(cls, client, account):
        user_data = {
            "_id": account.id,
            "username": account.username,
            "nickname": account.nickname,
            "roleId": account.role_id,
            "status": account.status,
        }
        token = get_jwt_token(user_data)
        client.credentials(HTTP_AUTHORIZATION=token)


    @classmethod
    def init_account(cls, username : str = None, password: str = None):

        username = username or uuid.uuid4().hex
        password = password or uuid.uuid4().hex
        role = Role.objects.get(role_name="访客")
        account = Account(
            username = username,
            nickname= username,
            password = password,
            role = role,
        )
        account.save()
        return account

    @classmethod
    def create_post(cls, user: Account):
        data = {
            "title": "title",
            "abstract": "abstract",
            "content": "content",
            "remark": "remark",
            "category": "category",
            "is_reship": False,
            "is_reship_url": "is_reship_url",
            "is_reship_name": "is_reship_name",
            "recommended": False,
            "like_token": [],
            "user": user
        }
        return BlogPost.objects.create( **data)


class AccountTestCase(BaseTestCase):
    def setUp(self) -> None:
        self.account = self.init_account()
        self.set_account_token(self.client, self.account)
        self.create_post(self.account)