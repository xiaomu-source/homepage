from blog.models import BlogPost
from blog.test import BaseTestCase, AccountTestCase

class AdminPostTestCase(AccountTestCase):
    def test_list(self):
        url = "/v1/blog/blog_articles/get-list/"
        data = {
            "pagination": {
                "current": 1,
                "pageSize": 10,
            },
            "sort": {
                "columnKey": "createdAt",
                "order": "ascend",
            },
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        url = "/v1/blog/blog_articles/create-blog/"
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
                "like_token": ["like_token"],
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        url = "/v1/blog/blog_articles/delete-blog/"
        data = {"_id": BlogPost.objects.first().id}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)


    def test_update(self):
        url = "/v1/blog/blog_articles/update-blog/"
        data = {
            "_id": (_id := BlogPost.objects.first().id),
            "title": "day01",
            "cover": "http://www.askmedo.cn/media/img.png",
            "abstract": "123456",
            "content": "123456",
            "category": "随记",
            "viewNum": 7,
            "likeNum": 0,
            "isReship": False,
            "recommended": False,
            "likeToken": None,
            "status": True,
            "createdAt": "2023-12-07 22:21:16",
            "updatedAt": "2023-12-08 18:02:04"
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)
        detail = self.client.post("/v1/blog/blog_articles/client/get-detail/", data={"_id": _id})
        self.assertEqual(detail.data["data"]["title"], data["title"])



class ClientPostTestCase(BaseTestCase):
    def test_list(self):
        url = "/v1/blog/blog_articles/client/get-list/"

        data = {
            "params": {},
            "pagination": {
            "total": 0,
            "pageSize": 10,
            "current": 1
            }
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        url = "/v1/blog/blog_articles/client/get-detail/"
        data = {"_id": BlogPost.objects.first().id}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)

    def test_relate(self):
        url = "/v1/blog/blog_articles/client/relate/"
        data = {"_id": {"_id": BlogPost.objects.first().id}}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)

    def test_like(self):
        url = "/v1/blog/blog_articles/client/like/"
        data = {"_id": BlogPost.objects.first().id}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)


class AdminMessageTestCase(AccountTestCase):
    def test_list(self):
        url = "/v1/blog/messages/get-list/"
        data = {
            "params": {},
            "pagination": {
                "total": 0,
                "pageSize": 10,
                "current": 1
            }
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        pass

    def test_delete(self):
        pass

    def test_update(self):
        pass