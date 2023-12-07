from blog.test import AccountTestCase


class UserTestCase(AccountTestCase):
    def test_find_one(self):
        url = "/v1/sys/users/findOne/"
        response = self.client.post(url,data={"_id": self.account.id})
        self.assertEqual(response.status_code, 200)

