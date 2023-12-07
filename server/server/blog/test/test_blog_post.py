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
        data = {"_id": (id := BlogPost.objects.first().id), "title": (title := "狗哥是个 gay")}
        response = self.client.post(url, data=data)
        blog_post = BlogPost.objects.get(id = id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(blog_post.title, title)



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