from django.core.exceptions import ObjectDoesNotExist
import re

from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from blog.models import BlogPost, Reply, Message, Portfolio
from blog.serializers import BlogPostSerializer, MessageSerializer, PortfolioSerializer
from utils.authentications import AccountViewSet, CSRFExemptViewSet
from utils.decorator import schema_required, check_api_permission, action_record
from utils.files import get_filename_from_media_url
from utils.response import APIResponse, BadResponse
from utils.user import get_public_ip, make_password, get_email_avatar, parse_ip, get_browser
from system.models import Account, Role
from utils.utils import dict_remove_empty_key, get_list_view_data, filter_queryset_by_partial_match
from utils.validations import StrField, BoolField, EmailField


class AdminPostViewSet(AccountViewSet):

    @schema_required(with_list=True)
    @check_api_permission("blog:blog_articles:list")
    @action(methods=["post"], detail=False, url_path="get-list")
    def get_list(self, request):
        try:
            return APIResponse(get_list_view_data(BlogPost, BlogPostSerializer, self.validated_data))
        except Exception as e:
            return BadResponse(str(e))

    @schema_required(
        under_sore=True,
        title=StrField(required=False,help_text=""),
        status=BoolField(required=False,help_text=""),
        recommended=BoolField(required=False,help_text=""),
        isReshipUrl=StrField(required=False,help_text=""),
        isReshipName=StrField(required=False,help_text=""),
        isReship=BoolField(required=False,help_text=""),
        cover=StrField(required=False,help_text=""),
        content=StrField(required=False,help_text=""),
        category=StrField(required=False,help_text=""),
        abstract=StrField(required=False,help_text=""),
    )
    @check_api_permission("blog:blog_articles:create")
    @action_record("博文管理/创建")
    @action(methods=["post"], detail=False, url_path="create-blog")
    def create_blog(self, request):
        with transaction.atomic():
            try:
                self.validated_data["user"] = request.user
                self.validated_data["cover"] = get_filename_from_media_url(self.validated_data.get("cover"))
                blog_post = BlogPost.objects.create(**self.validated_data)
                return APIResponse(BlogPostSerializer(blog_post).data)
            except Exception as e:
                return BadResponse(str(e))

    @schema_required(
        under_sore=True,
        with_id=True,
        title=StrField(required=False, help_text=""),
        status=BoolField(required=False, help_text=""),
        recommended=BoolField(required=False, help_text=""),
        isReshipUrl=StrField(required=False, help_text=""),
        isReshipName=StrField(required=False, help_text=""),
        isReship=BoolField(required=False, help_text=""),
        cover=StrField(required=False, help_text=""),
        content=StrField(required=False, help_text=""),
        category=StrField(required=False, help_text=""),
        abstract=StrField(required=False, help_text=""),
    )
    @check_api_permission("blog:blog_articles:update")
    @action_record("博文管理/更新")
    @action(methods=["post"], detail=False, url_path="update-blog")
    def update_blog(self, request):
        with transaction.atomic():
            try:
                self.validated_data["cover"] = get_filename_from_media_url(self.validated_data.get("cover"))
                BlogPost.objects.filter(pk=self.validated_data.pop("id")).update(**self.validated_data)
                return APIResponse("博文管理更新成功.")
            except Exception as e:
                return BadResponse(str(e))

    @schema_required(with_id=True)
    @check_api_permission("blog:blog_articles:delete")
    @action_record("博文管理/删除")
    @action(methods=["post"], detail=False, url_path="delete-blog")
    def delete_blog(self, request):
        try:
            BlogPost.objects.filter(pk=self.validated_data.get("id")).delete()
            return APIResponse("删除博文管理成功")
        except Exception as e:
            return BadResponse(str(e))

    @action(methods=["post"], detail=False, url_path="uploadMd")
    def upload_md(self, request):
        try:
            uploaded_file = request.FILES.get('file')
            if not uploaded_file:
                return Response({"message": "没有上传文件"}, status=status.HTTP_400_BAD_REQUEST)

            file_content = uploaded_file.read().decode('utf-8')

            # Extract image URLs from the Markdown content
            img_src_regex = r'<img[^>]+src="([^">]+)"'
            img_src_matches = re.findall(img_src_regex, file_content)
            image_urls = img_src_matches if img_src_matches else []

            # Extract plain text excerpt
            excerpt_length = 300
            replace_str_mapping = ["~", "#", "*", "\n", "\t", "\r",]
            plain_text_excerpt = "".join([s for s in file_content[:excerpt_length] if s not in replace_str_mapping])

            data = {
                "filename": uploaded_file.name,
                "fileData": file_content,
                "imageUrls": image_urls,
                "plainTextExcerpt": plain_text_excerpt
            }
            return APIResponse(data)

        except Exception as e:
            return BadResponse(str(e))


class ClientPostViewSet(CSRFExemptViewSet):
    @schema_required(with_list=True)
    @action(methods=["post"], detail=False, url_path="get-list")
    def get_list(self, request):
        try:
            return APIResponse(get_list_view_data(BlogPost, BlogPostSerializer, self.validated_data))
        except Exception as e:
            return BadResponse(str(e))

    @schema_required(with_id=True)
    @action(methods=["post"], detail=False, url_path="get-detail")
    def get_detail(self, request):
        try:
            blog_article = BlogPost.objects.get(pk=self.validated_data.get("id"))
            blog_article.view_num = (blog_article.view_num or 0) + 1
            blog_article.save()
            serialized_data = BlogPostSerializer(blog_article).data
            return APIResponse(serialized_data, message="博文详情查询成功.")
        except BlogPost.DoesNotExist:
            return BadResponse("该博文不存在")
        except Exception as e:
            return BadResponse(str(e))

    @schema_required(with_id=True)
    @action(methods=["post"], detail=False, url_path="relate")
    def relate(self, request):
        try:
            blog_post = BlogPost.objects.get(pk=self.validated_data.get("id"))
            related_articles = BlogPost.objects.filter(category__icontains=blog_post.category).exclude(pk=blog_post.pk)
            return APIResponse(BlogPostSerializer(related_articles, many=True).data)
        except Exception as e:
            return BadResponse(str(e))

    @schema_required(with_id=True)
    @action(methods=["post"], detail=False, url_path="like")
    def like(self, request):
        try:
            blog_article = BlogPost.objects.get(pk=self.validated_data.get("id"))

            # Check if the request contains a 'temptoken'
            temptoken = request.headers.get('temptoken')
            like_tokens = blog_article.like_token or []

            if not temptoken:
                # Generate a temporary token
                # Implement your own way to generate a token, such as creating a hash from user's IP
                temptoken = get_public_ip(request)
                # Save the temporary token to the blog article to mark it as liked
                blog_article.like_token = [temptoken]
                blog_article.save()
                return APIResponse({ "token": temptoken})

            # Check if the blog article contains the provided 'temptoken' to avoid duplicate likes
            if temptoken in (blog_article.like_token or []):
                return APIResponse("您已经点赞过该博文.")

            # Update the like count and save it back to the database
            blog_article.like_num = (blog_article.like_num or 0) + 1
            blog_article.like_token = like_tokens.append(temptoken)
            blog_article.save()

            return APIResponse("")

        except ObjectDoesNotExist:
            return BadResponse("该博文不存在")

        except Exception as e:
            return BadResponse(str(e))


class AdminMessageViewSet(AccountViewSet):
    @schema_required(with_list=True)
    @check_api_permission('blog:messages:list')
    @action(methods=["post"], detail=False, url_path="get-list")
    def get_list(self, request):
        model_objs = filter_queryset_by_partial_match(Message, self.validated_data.get("params"))
        if order_by_filed := self.validated_data.get("order_by_field"):
            model_objs = model_objs.order_by(order_by_filed)
        model_objs = self.slice_query(model_objs)
        return APIResponse({
            'result': MessageSerializer(model_objs, many=True).data,
            'current': self.validated_data.get("current"),
            'pageSize': self.validated_data.get("page_size"),
            'total': model_objs.count(),
            'repliesCount': Reply.objects.filter(message_id__in=[obj.id for obj in model_objs]).count()
        })

    @schema_required(
        content=StrField(required=True, help_text="留言内容"),
    )
    @check_api_permission('blog:messages:create')
    @action(methods=["post"], detail=False, url_path="create-message")
    def create_message(self, request):
        content = self.validated_data.get('content')
        Message.objects.create(content=content, user=request.user)
        return APIResponse({'content': content, 'user': request.user.id,})

    @schema_required(
        with_id=True,
        pid=StrField(required=True)
    )
    @check_api_permission('blog:messages:delete')
    @action(methods=["post"], detail=False, url_path="delete-message")
    def delete_message(self, request):
        _id = self.validated_data.get("id")
        pid = self.validated_data.get('pid')
        if pid:
            deleted, _ = Reply.objects.filter(message_id=id).delete()
            if not deleted:
                return BadResponse("该留言不存在或已被删除")
            return APIResponse("删除留言成功")
        # 首先删除关联的ReplyModel数据
        Reply.objects.filter(message_id=_id).delete()
        # 删除与留言关联的ReplyModel数据成功后，再删除留言自身
        deleted, _ = Message.objects.filter(id=_id).delete()
        if not deleted:
            return BadResponse("该留言不存在或已被删除")
        return APIResponse("删除留言成功")

    @schema_required(
        with_id=True,
        pid=StrField(required=True),
        content=StrField(required=True, help_text="留言内容"),
    )
    @check_api_permission('blog:messages:update')
    @action(methods=["post"], detail=False, url_path="update-message")
    def update_message(self, request):
        _id = self.validated_data.get('_id')
        pid = self.validated_data.data.get('pid')
        content = self.validated_data.get('content')

        if pid:
            reply_info = Reply.objects.filter(id=_id).first()
            if not reply_info:
                return BadResponse("该留言不存在")
            # 更新留言数据.
            reply_info.content = content if content else reply_info.content
            reply_info.save()
        messages_info = Message.objects.filter(id=_id).first()
        if not messages_info:
            return BadResponse("该留言不存在")
        # 更新留言数据.
        messages_info.content = content if content else messages_info.content
        messages_info.save()

        return APIResponse("留言更新成功")


class ClientMessageViewSet(CSRFExemptViewSet):
    @schema_required(with_list=True)
    @action(methods=["post"], detail=False, url_path="get-list")
    def get_list(self, request):
        model_objs = filter_queryset_by_partial_match(Message, self.validated_data.get("params"))
        if order_by_filed := self.validated_data.get("order_by_field"):
            model_objs = model_objs.order_by(order_by_filed)
        model_objs = self.slice_query(model_objs)
        return APIResponse({
            'result': MessageSerializer(model_objs, many=True).data,
            'current': self.validated_data.get("current"),
            'pageSize': self.validated_data.get("page_size"),
            'total': model_objs.count(),
            'repliesCount': Reply.objects.filter(message_id__in=[obj.id for obj in model_objs]).count()
        })

    @schema_required(
        name=StrField(required=False, help_text="用户昵称"),
        email=EmailField(required=True, help_text="用户邮箱"),
        website=StrField(required=True, help_text="用户站点"),
        content=StrField(required=True, help_text="留言内容"),
    )
    @action(methods=["post"], detail=False, url_path="create-message")
    def create_message(self, request):
        try:
            content = self.validated_data.get('content')
            name = self.validated_data.get('name')
            email = self.validated_data.get('email')
            website = self.validated_data.get('website')
            # 查找是否存在该用户
            user = Account.objects.filter(email=email, status=True).first()
            # 识别常见的浏览器、操作系统和设备等信息
            client_ip = get_public_ip(request)
            address = parse_ip(client_ip)
            platform = get_browser(request)

            if not user:
                password = make_password(email)
                avatar = get_email_avatar(email)
                user_data = dict(
                    type='user', # 默认前台用户
                    nickname=name if name else '匿名',
                    avatar=avatar,
                    userIp=client_ip,
                    website=website,
                    address=address,
                    platform=platform,
                    password=password,
                    email=email,
                    username=email,
                    role=Role.objects.get(role_auth="VISITOR-ADMIN")
                )
                user = Account(**dict_remove_empty_key(user_data))
            else:
                user.userIp = client_ip
                user.website = website
            user.save()

            Message.objects.create(
                content=content,
                user=user
            )

            return APIResponse("填加留言成功")

        except Exception as e:
            return BadResponse(str(e))

    @schema_required(
        message=StrField(required=True, help_text="消息ID"),
        toUser=StrField(required=True, help_text="回复用户ID"),
        name=StrField(required=False, help_text="用户昵称"),
        email=EmailField(required=True, help_text="用户邮箱"),
        website=StrField(required=True, help_text="用户站点"),
        content=StrField(required=True, help_text="留言内容"),
    )
    @action(methods=["post"], detail=False, url_path="reply")
    def reply(self, request):
        try:
            content = self.validated_data.get('content')
            message_id = int(self.validated_data.get('message'))
            message = Message.objects.get(id=message_id)
            to_user_id = self.validated_data.get('to_user')
            name = self.validated_data.get('name')
            email = self.validated_data.get('email')
            website = self.validated_data.get('website')
            # 查找是否存在该用户
            user = Account.objects.filter(email=email, status=True).first()
            # 如果用户不存在，则创建用户
            if not user:
                client_ip = get_public_ip(request)
                address = parse_ip(client_ip)
                platform = get_browser(request)
                password = make_password(email)
                avatar = get_email_avatar(email)
                user_data = dict(
                    type='user',
                    nickname=name if name else '匿名',
                    avatar=avatar,
                    userIp=client_ip,
                    website=website,
                    address=address,
                    platform=platform,
                    password=password,
                    email=email,
                    username=email,
                    role=Role.objects.get(role_auth="VISITOR-ADMIN")
                )
                user = Account(**dict_remove_empty_key(user_data))
                user.save()

            Reply.objects.create(
                content=content,
                message=message,
                to_user=to_user_id,
                user=user.id,
            )

            return APIResponse("回复成功")

        except Exception as e:
            return BadResponse(str(e))

    @schema_required(with_id=True)
    @action(methods=["post"], detail=False, url_path="like")
    def like(self, request):
        try:
            message = get_object_or_404(Message, pk=self.validated_data.get("id"))

            message.like_num = (message.like_num or 0) + 1
            message.save()

            return APIResponse("点赞成功")

        except Exception as e:
            return BadResponse(str(e))

    @schema_required(with_id=True)
    @action(methods=["post"], detail=False, url_path="opposeNum")
    def oppose_num(self, request):
        try:
            message = get_object_or_404(Message, pk=self.validated_data.get("id"))

            message.oppose_num = (message.oppose_num or 0) + 1
            message.save()

            return APIResponse("操作成功")

        except Exception as e:
            return BadResponse(str(e))


class AdminPortfolioViewSet(AccountViewSet):
    @schema_required(with_list=True)
    @check_api_permission('blog:portfolios:list')
    @action(methods=["post"], detail=False, url_path="get-list")
    def get_list(self, request):
        try:
            return APIResponse(get_list_view_data(Portfolio, PortfolioSerializer, self.validated_data))
        except Exception as e:
            return BadResponse(str(e))
    
    @schema_required(
        under_sore=True,
        title=StrField(required=True, help_text=""),
        cover=StrField(required=False, help_text=""),
        abstract=StrField(required=False, help_text=""),
        content=StrField(required=False, help_text=""),
        source_url=StrField(required=False, help_text=""),
        demo_url=StrField(required=False, help_text=""),
        user=StrField(required=False, help_text=""),
        remark=StrField(required=False, help_text=""),
        category=StrField(required=False, help_text=""),
        framework=StrField(required=False, help_text=""),
        recommended=BoolField(required=False, help_text=""),
        status=BoolField(required=False, help_text=""),
    )
    @check_api_permission('blog:portfolios:create')
    @action_record("作品集/创建")
    @action(methods=["post"], detail=False, url_path="create-portfolio")
    def create_portfolio(self, request):
        try:
            self.validated_data["user"] = request.user
            Portfolio.objects.create(**self.validated_data).save()
            return APIResponse("创建成功")
        except Exception as e:
            return BadResponse(str(e))

    @schema_required(with_id=True)
    @check_api_permission('blog:portfolios:delete')
    @action_record("作品集/删除")
    @action(methods=["post"], detail=False, url_path="delete-portfolio")
    def delete_portfolio(self, request):
        try:
            portfolio = get_object_or_404(Portfolio, id=self.validated_data.get("id"))
            portfolio.delete()
            return APIResponse("Portfolio deleted successfully")
        except Exception as e:
            return BadResponse( str(e))

    @schema_required(
        with_id=True,
        under_sore=True,
        title=StrField(required=True, help_text=""),
        cover=StrField(required=False, help_text=""),
        abstract=StrField(required=False, help_text=""),
        content=StrField(required=False, help_text=""),
        source_url=StrField(required=False, help_text=""),
        demo_url=StrField(required=False, help_text=""),
        user=StrField(required=False, help_text=""),
        remark=StrField(required=False, help_text=""),
        category=StrField(required=False, help_text=""),
        framework=StrField(required=False, help_text=""),
        recommended=BoolField(required=False, help_text=""),
        status=BoolField(required=False, help_text=""),
    )
    @check_api_permission('blog:portfolios:update')
    @action_record("作品集/更新")
    @action(methods=["post"], detail=False, url_path="update-portfolio")
    def update_portfolio(self, request):
        try:
            _id = self.validated_data.pop("id")
            Portfolio.objects.filter(pk=_id).update(**self.validated_data)
            return APIResponse("Portfolio updated successfully")
        except Exception as e:
            return BadResponse(str(e))


class ClientPortfolioViewSet(CSRFExemptViewSet):

    @schema_required(with_list=True)
    @action(methods=["post"], detail=False, url_path="get-list")
    def get_list(self, request):
        try:
            return APIResponse(get_list_view_data(Portfolio, PortfolioSerializer, self.validated_data))
        except Exception as e:
            return BadResponse(str(e))

    @schema_required(with_id=True)
    @action(methods=["post"], detail=False, url_path="get-detail")
    def get_detail(self, request):
        try:
            portfolio = Portfolio.objects.get(_id=self.validated_data.get("id"))
            return APIResponse(PortfolioSerializer(portfolio).data)
        except Exception as e:
            return BadResponse(str(e))