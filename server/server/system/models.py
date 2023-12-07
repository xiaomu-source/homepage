import uuid

from django.db import models


class Permission(models.Model):
    name = models.CharField(max_length=64, verbose_name="权限名称")
    key = models.CharField(max_length=256, verbose_name="权限健")
    parent_key = models.CharField(max_length=256, verbose_name="父级权限键（可选）", blank=True, null=True)
    auth = models.BooleanField(default=False, verbose_name="是否是权限按钮")
    sort_order = models.IntegerField(default=0, verbose_name="排序字段")
    status = models.BooleanField(default=True, verbose_name="状态：0正常 1禁用")
    disabled = models.BooleanField(default=False, verbose_name="状态：0正常 1禁用")
    created_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新时间", auto_now=True, db_index=True)


    class Meta:
        verbose_name = "权限"
        verbose_name_plural = "权限"

    # 添加静态方法: 转换为树状结构
    @staticmethod
    def to_tree(permissions):
        tree = []
        node_map = {}

        for permission in permissions:
            node_map[permission.key] = permission

        for permission in permissions:
            parent = node_map.get(permission.parent_key or "")
            if parent:
                children = getattr(parent, "children", [])
                children.append(node_map[permission.key])
                parent.children = children
            else:
                tree.append(node_map[permission.key])

        return tree

    # 添加静态方法: 转换为扁平结构
    @staticmethod
    def to_flat(permissions):
        flat = []

        def flatten(permission, parent_key=None):
            flat_permission = {**permission, 'parent_key': parent_key}
            flat.append(flat_permission)

            if 'children' in permission:
                for child in permission['children']:
                    flatten(child, permission['key'])

        for permission in permissions:
            flatten(permission)

        return flat


class Role(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True)
    role_name = models.CharField(max_length=64, unique=True, db_index=True, verbose_name="角色名称")
    role_auth = models.CharField(max_length=64, verbose_name="角色标识")
    perms = models.JSONField(verbose_name="权限类别", blank=True, null=True)
    remark = models.CharField(max_length=256, verbose_name="备注", blank=True, null=True)
    status = models.BooleanField(default=True, verbose_name="状态: 0禁用 1正常")
    created_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新时间", auto_now=True, db_index=True)


    class Meta:
        verbose_name = "角色"
        verbose_name_plural = "角色"


class Account(models.Model):
    avatar = models.CharField(max_length=256, verbose_name="用户头像", blank=True)
    username = models.CharField(max_length=64, verbose_name="用户名")
    nickname = models.CharField(max_length=64, verbose_name="昵称")
    password = models.CharField(max_length=256, verbose_name="密码")
    email = models.CharField(max_length=64, verbose_name="邮箱", blank=True)
    role = models.ForeignKey(Role, verbose_name="角色", on_delete=models.DO_NOTHING)
    remark = models.CharField(max_length=256, verbose_name="备注", blank=True, null=True)
    status = models.BooleanField(default=True, verbose_name="状态: 0禁用 1正常")
    type = models.CharField(max_length=16, choices=(("admin", "admin"),("user", "user")), default="admin",verbose_name="用户角色")
    website = models.CharField(max_length=256, verbose_name="用户站点", blank=True)
    platform = models.CharField(max_length=128, verbose_name="操作平台", blank=True)
    userIp = models.CharField(max_length=128, verbose_name="设备IP", default="0.0.0.0")
    address = models.CharField(max_length=256, verbose_name="设备位置", blank=True)
    created_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新时间", auto_now=True, db_index=True)

    class Meta:
        verbose_name = "权限"
        verbose_name_plural = "权限"


class Resource(models.Model):
    src_name = models.CharField(max_length=128, verbose_name="资源名称")
    src_type = models.CharField(max_length=64, verbose_name="资源类型")
    preview_path = models.CharField(max_length=256, verbose_name="资源预览路径")
    download_path = models.CharField(max_length=256, verbose_name="资源下载路径")
    delete_path = models.CharField(max_length=256, verbose_name="资源删除路径")
    user = models.ForeignKey(Account, verbose_name="用户", on_delete=models.DO_NOTHING)
    src_size = models.CharField(max_length=256, verbose_name="资源大小")
    remark = models.CharField(max_length=256, verbose_name="备注")
    status = models.BooleanField(default=True, verbose_name="状态: false禁用 true正常")
    created_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新时间", auto_now=True, db_index=True)

    class Meta:
        verbose_name = "资源"
        verbose_name_plural = "资源"


class UserOptLog(models.Model):
    operator = models.CharField(max_length=64, verbose_name="操作人")
    operator_id = models.CharField(max_length=256, verbose_name="操作人ID", blank=True, null=True)
    module = models.CharField(max_length=256, verbose_name="操作模块")
    platform = models.CharField(max_length=256, verbose_name="操作平台")
    operator_ip = models.CharField(max_length=256, verbose_name="设备IP")
    address = models.CharField(max_length=256, verbose_name="设备位置")
    content = models.CharField(max_length=256, verbose_name="操作内容", blank=True, null=True)
    created_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新时间", auto_now=True, db_index=True)

    class Meta:
        verbose_name = "操作记录"
        verbose_name_plural = "操作记录"