from rest_framework import serializers

from blog.models import BlogPost, Message, Portfolio, Reply
from system.models import Account
from system.serializers import AccountSerializer
from utils.files import get_media_url
from utils.user import get_user_info


class BlogPostSerializer(serializers.ModelSerializer):
    _id = serializers.IntegerField(source="id")
    viewNum = serializers.IntegerField(source="view_num")
    likeNum = serializers.IntegerField(source="like_num")
    isReship = serializers.BooleanField(source="is_reship")
    likeToken = serializers.CharField(source="like_token")
    createdAt = serializers.DateTimeField(source="created_at")
    updatedAt = serializers.DateTimeField(source="updated_at")
    user = serializers.SerializerMethodField()
    cover = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = ["_id", "title", "cover", "abstract", "content", "user", "category", "viewNum", "likeNum", "isReship",
                  "recommended", "likeToken", "status", "createdAt", "updatedAt"]

    def get_user(self, obj) -> list[dict]:
        return get_user_info(obj.user)

    def get_cover(self, obj) -> str:
        return get_media_url(obj.cover)


class MessageSimpleSerializer(serializers.ModelSerializer):
    _id = serializers.IntegerField(source="id")
    user = serializers.IntegerField(source="user.id")
    likeNum = serializers.IntegerField(source="like_num")
    opposeNum = serializers.IntegerField(source="oppose_num")
    createdAt = serializers.DateTimeField(source="created_at")
    updatedAt = serializers.DateTimeField(source="updated_at")

    class Meta:
        model = Message
        fields = ["_id", "content", "hidden", "user", "likeNum", "opposeNum", "createdAt", "updatedAt",]


class ReplySerializer(serializers.ModelSerializer):
    _id = serializers.IntegerField(source="id")
    userInfo = serializers.SerializerMethodField()
    toUserInfo = serializers.SerializerMethodField()
    messageInfo = MessageSimpleSerializer(source="message")
    createdAt = serializers.DateTimeField(source="created_at")
    updatedAt = serializers.DateTimeField(source="updated_at")

    class Meta:
        model = Reply
        fields = ["_id", "userInfo", "toUserInfo", "messageInfo", "content", "createdAt", "updatedAt",]

    def get_userInfo(self, obj):
        user = Account.objects.get(id=obj.user)
        return AccountSerializer(user).data

    def get_toUserInfo(self, obj):
        to_user = Account.objects.get(id=obj.to_user)
        return AccountSerializer(to_user).data


class MessageSerializer(serializers.ModelSerializer):
    _id = serializers.IntegerField(source="id")
    repliesInfo = serializers.SerializerMethodField()
    likeNum = serializers.IntegerField(source="like_num")
    opposeNum = serializers.IntegerField(source="oppose_num")
    createdAt = serializers.DateTimeField(source="created_at")
    updatedAt = serializers.DateTimeField(source="updated_at")
    userInfo = serializers.SerializerMethodField()


    class Meta:
        model = Message
        fields = ["_id", "content", "hidden", "likeNum", "opposeNum", "repliesInfo", "content", "createdAt", "updatedAt","userInfo"]

    def get_repliesInfo(self, obj):
        if not obj.reply_id:
            replies = Reply.objects.filter(message_id=obj.id)
            return ReplySerializer(replies, many=True).data
        replies = Reply.objects.filter(id=obj.reply_id)
        return ReplySerializer(replies, many=True).data

    def get_userInfo(self, obj):
        return [AccountSerializer(obj.user).data]

class PortfolioSerializer(serializers.ModelSerializer):
    _id = serializers.IntegerField(source="id")
    sourceUrl = serializers.CharField(source="source_url")
    demoUrl = serializers.CharField(source="demo_url")
    userInfo = AccountSerializer(source="user")
    createdAt = serializers.DateTimeField(source="created_at")
    updatedAt = serializers.DateTimeField(source="updated_at")
    class Meta:
        model = Portfolio
        fields = ["_id", "title", "cover", "abstract", "content", "sourceUrl", "demoUrl", "remark", "category", "framework",
                  "recommended", "status", "createdAt", "updatedAt", "userInfo"]