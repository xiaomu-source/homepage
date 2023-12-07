import jwt

from django.test import TestCase


class JWTTestCase(TestCase):
    def test_jwt_decode(self):
        jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVzZXJuYW1lIiwibmlja25hbWUiOiJuaWNrbmFtZSJ9.LbTcUqzk4ZYkhfT6KERqVIRHFmrJ3d4O2dtm03LiUn8"
        expected = {"username": "username", "nickname": "nickname"}
        actual = jwt.decode(jwt_token, "key", algorithms=["HS256"])
        self.assertEqual(expected, actual)