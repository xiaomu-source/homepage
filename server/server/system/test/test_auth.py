from rest_framework.test import APITestCase

from system.models import Role, Account


class AuthTestCase(APITestCase):
    def test_register(self):
        url = "/v1/sys/auth/register/"
        data = {
            "username" : "username1",
            "nickname" : "nickname1",
            "password" : "password1",
            "roleId": Role.objects.get(role_name="访客").id
        }
        self.client.post(url, data=data)
        account = Account.objects.get(username=data["username"])
        self.assertTrue(account)

        url = "/v1/sys/auth/login/"
        data = {
            "username" : "username1",
            "nickname" : "nickname1",
            "password" : "password1",
        }
        response = self.client.post(url, data=data)
        self.assertTrue(data["username"], response.data["data"]["username"])

    def test_captcha(self):
        url = "/v1/sys/auth/captcha/"
        response = self.client.post(url)
        self.assertTrue(response.status_code, 200)

