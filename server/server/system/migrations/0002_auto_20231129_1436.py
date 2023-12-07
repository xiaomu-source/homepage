# Generated by Django 4.2.7 on 2023-11-29 06:36
from uuid import UUID

from django.db import migrations


def init_roles(apps, schema_editor):
    super_admin = {
        "uid": UUID('b55bde6e-2517-476d-9d5f-1440e4c8bff1'),
        "role_name": "超级管理员",
        "role_auth": "SUPER-ADMIN",
        "perms": ["*"],
        "remark": "拥有所有权限",
        "status": True,
    }
    normal_admin = {
        "uid": UUID('cf025ab9-c54e-4bd9-9260-3e84bd8fed3d'),
        "role_name": "普通管理员",
        "role_auth": "NORMALL-ADMIN",
        "perms": ["index", "sys:users:list", "sys:roles:list", "sys:permissions:list"],
        "remark": "拥有部分权限",
        "status": True,
    }
    dev_admin = {
        "uid": UUID('575a9751-97f8-4302-bfa7-8a0b1c5e0e35'),
        "role_name": "开发人员",
        "role_auth": "DEV-ADMIN",
        "perms": ["index", "dev", "dev:codes", "dev:codes:delete", "dev:icon", "dev:codes:list",
                  "dev:codes:singleCurdFrontAndBack", "dev:codes:deleteAll", "sys:resources", "sys:resources:list",
                  "sys:resources:create", "sys:resources:delete", "sys:resources:update"],
        "remark": "开发人员",
        "status": True,
    }
    visitor_admin = {
        "uid": UUID('a56b38e7-b16e-4236-9f03-1dc49ae49850'),
        "role_name": "访客",
        "role_auth": "VISITOR-ADMIN",
        "perms": ["index", "components:echart:chinaMap", "components:echart:worldMap", "components:echart:line",
                  "components:echart:pie", "pages", "pages:all", "dev:icon", "dev:codes:list", "components:editor",
                  "components:editor:Tinymce", "components:editor:Vditor", "components:editor:VMdEditor", "components",
                  "components:echart", "components:echart:guizhouMap", "sys:permissions:list",
                  "blog:blog_articles:list", "blog:portfolios:list", "blog:messages:list", "blog:messages:delete"],
        "remark": "一般访客，更多的是有查看权限",
        "status": True,
    }
    Role = apps.get_model("system", "Role")
    Account = apps.get_model("system", "Account")
    objs = [Role(**super_admin), Role(**normal_admin), Role(**dev_admin), Role(**visitor_admin), ]
    Role.objects.bulk_create(objs)
    Account.objects.create(username = "admin", nickname = "admin", password = "pbkdf2_sha256$600000$LRFWIA4Wi1P7l6aTwz8iPO$0jHBDmo15ImgOjSC3FgB/du38XkBKytORPFlCB5HA44=",
                           role = Role.objects.get(role_name="超级管理员"))

def init_permissions(apps, schema_editor):
    permissions = [
        (False, False,'index', '首页', 0, True, None),
        (False, False,'sys', '系统管理', 0, True, None),
        (False, False,'sys:users', '用户管理', 0, True, 'sys'),
        (True, False, 'sys:users:list', '查询', 0, True, 'sys:users'),
        (True, False, 'sys:users:create', '增加', 0, True, 'sys:users'),
        (True, False, 'sys:users:delete', '删除', 0, True, 'sys:users'),
        (True, False, 'sys:users:reset', '重置密码', 0, True, 'sys:users'),
        (False, False,'dev', '开发工具', 0, True, None),
        (False, False,'dev:icon', '图标列表', 1, True, 'dev'),
        (True, False, 'sys:permissions:list', '查询', 0, True, 'sys:permissions'),
        (True, False, 'sys:permissions:create', '增加', 0, True, 'sys:permissions'),
        (True, False, 'sys:permissions:delete', '删除', 0, True, 'sys:permissions'),
        (True, False, 'sys:permissions:update', '修改', 0, True, 'sys:permissions'),
        (False, False,'sys:roles', '角色管理', 0, True, 'sys'),
        (True, False, 'sys:roles:list', '查询', 0, True, 'sys:roles'),
        (True, False, 'sys:roles:create', '增加', 0, True, 'sys:roles'),
        (True, False, 'sys:roles:delete', '删除', 0, True, 'sys:roles'),
        (True, False, 'sys:roles:update', '更新', 0, True, 'sys:roles'),
        (False, False,'sys:permissions', '权限管理', 0, True, 'sys'),
        (True, False, 'sys:permissions:stop', '停用', None, True, 'sys:permissions'),
        (False, False,'dev:codes', '代码生成', 0, True, 'dev'),
        (True, False, 'dev:codes:list', '查询', 0, True, 'dev:codes'),
        (True, False, 'dev:codes:singleCurdFrontAndBack', '创建', 0, True, 'dev:codes'),
        (True, False, 'dev:codes:delete', '删除', 0, True, 'dev:codes'),
        (True, False, 'dev:codes:deleteAll', '批量删除', 0, True, 'dev:codes'),
        (False, False,'pages', '页面示例', 0, True, None),
        (False, False,'components', '组件示例', 0, True, None),
        (False, False,'components:echart', '图表地图', 0, True, 'components'),
        (False, False,'components:echart:guizhouMap', '贵州地图', 0, True, 'components:echart'),
        (False, False,'components:echart:chinaMap', '中国地图', 0, True, 'components:echart'),
        (False, False,'components:echart:worldMap', '世界地图', 0, True, 'components:echart'),
        (False, False,'components:echart:line', '折线图', 0, True, 'components:echart'),
        (False, False,'components:echart:pie', '饼图', 0, True, 'components:echart'),
        (False, False,'pages:all', '综合页面', 0, True, 'pages'),
        (False, False,'components:editor', '富文本', 0, True, 'components'),
        (False, False,'components:editor:Tinymce', 'Tinymce', 0, True, 'components:editor'),
        (False, False,'components:editor:Vditor', 'Vditor', 0, True, 'components:editor'),
        (False, False,'components:editor:VMdEditor', 'VMdEditor', 0, True, 'components:editor'),
        (False, False,'sys:users_opt_logs', '操作日志', 0, True, 'sys'),
        (True, False, 'sys:users_opt_logs:list', '查询', 0, True, 'sys:users_opt_logs'),
        (True, False, 'sys:users_opt_logs:create', '增加', 0, True, 'sys:users_opt_logs'),
        (True, False, 'sys:users_opt_logs:delete', '删除', 0, True, 'sys:users_opt_logs'),
        (True, False, 'sys:users_opt_logs:update', '更新', 0, True, 'sys:users_opt_logs'),
        (True, False, 'sys:users_opt_logs:deleteAll', '批量删除', 0, True, 'sys:users_opt_logs'),
        (True, False, 'sys:users_opt_logs:export', '导出', 0, True, 'sys:users_opt_logs'),
        (True, False, 'sys:users_opt_logs:import', '导入', 0, True, 'sys:users_opt_logs'),
        (False, False,'sys:resources', '资源管理', 0, True, 'sys'),
        (True, False, 'sys:resources:list', '查询', 0, True, 'sys:resources'),
        (True, False, 'sys:resources:create', '增加', 0, True, 'sys:resources'),
        (True, False, 'sys:resources:delete', '删除', 0, True, 'sys:resources'),
        (True, False, 'sys:resources:update', '更新', 0, True, 'sys:resources'),
        (False, False,'blog', '博客管理', 0, True, None),
        (False, False,'blog:blog_articles', '博文管理', 0, True, 'blog'),
        (True, False, 'blog:blog_articles:list', '查询', 0, True, 'blog:blog_articles'),
        (True, False, 'blog:blog_articles:create', '增加', 0, True, 'blog:blog_articles'),
        (True, False, 'blog:blog_articles:delete', '删除', 0, True, 'blog:blog_articles'),
        (True, False, 'blog:blog_articles:update', '更新', 0, True, 'blog:blog_articles'),
        (False, False,'blog:portfolios', '作品管理', 0, True, 'blog'),
        (True, False, 'blog:portfolios:list', '查询', 0, True, 'blog:portfolios'),
        (True, False, 'blog:portfolios:create', '增加', 0, True, 'blog:portfolios'),
        (True, False, 'blog:portfolios:delete', '删除', 0, True, 'blog:portfolios'),
        (True, False, 'blog:portfolios:update', '更新', 0, True, 'blog:portfolios'),
        (False, False,'blog:messages', '留言管理', 0, True, 'blog'),
        (True, False, 'blog:messages:list', '查询', 0, True, 'blog:messages'),
        (True, False, 'blog:messages:create', '增加', 0, True, 'blog:messages'),
        (True, False, 'blog:messages:delete', '删除', 0, True, 'blog:messages'),
        (True, False, 'blog:messages:update', '更新', 0, True, 'blog:messages'),
    ]
    Permission = apps.get_model("system", "Permission")
    permission_objs = []
    for auth, disabled, key, name, sort_order, status, parent_key in permissions:
        permission_objs.append(
            Permission(auth=auth, disabled=disabled, key=key, name=name, sort_order=sort_order, status=status, parent_key=parent_key or "")
        )
    Permission.objects.bulk_create(permission_objs, ignore_conflicts=True)

class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [migrations.RunPython(init_roles), migrations.RunPython(init_permissions)]