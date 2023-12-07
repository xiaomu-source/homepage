from django.conf import settings
from rest_framework import serializers
from system.models import Account, Role, Permission, UserOptLog, Resource
from utils.files import get_media_url, get_media_delete_url


class AccountSerializer(serializers.ModelSerializer):
    _id = serializers.IntegerField(source="id")
    roleId = serializers.CharField(source="role.id")
    createdAt = serializers.DateTimeField(source="created_at")
    updatedAt = serializers.DateTimeField(source="updated_at")

    class Meta:
        model = Account
        fields = ["_id", "avatar", "username", "nickname", "password", "roleId", "status", "createdAt", "updatedAt",
                  "type", "email", "address", "userIp", "platform", "website",]

class RoleSerializer(serializers.ModelSerializer):
    _id = serializers.IntegerField(source="id")
    roleName = serializers.CharField(source="role_name")
    roleAuth = serializers.CharField(source="role_auth")
    createdAt = serializers.DateTimeField(source="created_at")
    updatedAt = serializers.DateTimeField(source="updated_at")
    class Meta:
        model = Role
        fields = ["_id", "uid", "roleName", "roleAuth", "perms", "remark", "status", "createdAt", "updatedAt",]


class PermissionSerializer(serializers.ModelSerializer):
    _id = serializers.IntegerField(source="id")
    createdAt = serializers.DateTimeField(source="created_at")
    updatedAt = serializers.DateTimeField(source="updated_at")
    children = serializers.SerializerMethodField()
    sortOrder = serializers.IntegerField(source="sort_order")

    class Meta:
        model = Permission
        fields = ["_id", "name", "key", "children", "auth", "sortOrder", "status", "disabled", "createdAt", "updatedAt",]

    def get_children(self, obj):
        children = getattr(obj, "children", [])
        if children:
            return PermissionSerializer(children, many=True).data
        return []


class UserOptLogSerializer(serializers.ModelSerializer):
    _id = serializers.IntegerField(source="id")
    createdAt = serializers.DateTimeField(source="created_at")
    updatedAt = serializers.DateTimeField(source="updated_at")
    operatorId = serializers.CharField(source="operator_id")
    operatorIp = serializers.CharField(source="operator_ip")
    class Meta:
        model = UserOptLog
        fields = ["_id", "operator", "operatorId", "module", "platform", "operatorIp", "address", "content", "createdAt", "updatedAt",]

class ResourceSerializer(serializers.ModelSerializer):
    _id = serializers.CharField(source="id")
    user = serializers.SerializerMethodField()
    userId = serializers.CharField(source="user.id")
    srcType = serializers.CharField(source="src_type")
    srcSize = serializers.CharField(source="src_size")
    srcName = serializers.CharField(source="src_name")
    previewPath = serializers.SerializerMethodField()
    downloadPath = serializers.SerializerMethodField()
    deletePath = serializers.SerializerMethodField()
    createdAt = serializers.DateTimeField(source="created_at")
    updatedAt = serializers.DateTimeField(source="updated_at")
    class Meta:
        model = Resource
        fields = ["_id", "user", "userId", "status", "srcType", "srcSize", "srcName", "previewPath", "downloadPath", "deletePath",
              "createdAt", "updatedAt", ]

    def get_previewPath(self, obj):
        return get_media_url(obj.src_name)

    def get_downloadPath(self, obj):
        return get_media_url(obj.src_name)

    def get_deletePath(self, obj):
        return get_media_delete_url(obj.src_name)

    def get_user(self, obj):
        return [AccountSerializer(obj.user).data]

