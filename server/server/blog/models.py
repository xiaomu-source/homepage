from django.db import models

from system.models import Account


class BlogPost(models.Model):
    title = models.CharField(max_length=64, verbose_name="博文名称")
    cover = models.CharField(max_length=256, verbose_name="博文封面", blank=True)
    abstract = models.CharField(max_length=256, blank=True, verbose_name="博文摘要")
    content = models.TextField(verbose_name="博文内容", help_text="正文必须为MarkDown格式")
    user = models.ForeignKey(Account, verbose_name="作者", on_delete=models.DO_NOTHING)
    remark = models.CharField(max_length=256, verbose_name="备注", blank=True)
    category = models.CharField(max_length=64, verbose_name="分类", blank=True)
    view_num = models.IntegerField(default=0, verbose_name="浏览量")
    like_num = models.IntegerField(default=0, verbose_name="点赞量")
    is_reship = models.BooleanField(default=False, verbose_name="是否转载")
    is_reship_url = models.CharField(max_length=256, verbose_name="转载文章地址", blank=True, null=True)
    is_reship_name = models.CharField(max_length=64, verbose_name="转载文章名称", blank=True, null=True)
    recommended = models.BooleanField(default=False, verbose_name="是否精选")
    like_token = models.JSONField(verbose_name="点赞的临时标识", blank=True, null=True)
    status = models.BooleanField(default=True, verbose_name="状态 发布和草稿")
    created_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新时间", auto_now=True, db_index=True)

    class Meta:
        verbose_name = "博客文章"
        verbose_name_plural = "博客文章"

class Message(models.Model):
    content = models.CharField(max_length=256, verbose_name="留言内容")
    hidden = models.BooleanField(default=False, verbose_name="是否隐藏")
    user = models.ForeignKey(Account, verbose_name="关联的用户ID", on_delete=models.DO_NOTHING)
    reply_id = models.IntegerField(verbose_name="关联的回复ID", blank=True, null=True)
    like_num = models.IntegerField(default=0, verbose_name="点赞量")
    oppose_num = models.IntegerField(default=0, verbose_name="反对量")
    created_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新时间", auto_now=True, db_index=True)

    class Meta:
        verbose_name = "留言"
        verbose_name_plural = "留言"

class Reply(models.Model):
    message = models.ForeignKey(Message, verbose_name="关联的留言ID", on_delete=models.DO_NOTHING)
    user = models.CharField(max_length=256, verbose_name="原始用户ID")
    to_user = models.CharField(max_length=256, verbose_name="目标用户ID")
    content = models.CharField(max_length=256, verbose_name="回复内容")
    created_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新时间", auto_now=True, db_index=True)

    class Meta:
        verbose_name = "回复"
        verbose_name_plural = "回复"

class Portfolio(models.Model):
    title = models.CharField(max_length=64, verbose_name="作品名称")
    cover = models.CharField(max_length=256, verbose_name="作品封面", blank=True)
    abstract = models.CharField(max_length=256, verbose_name="作品简介",)
    content = models.CharField(max_length=256, verbose_name="作品内容")
    source_url = models.CharField(max_length=256, verbose_name="源码地址", blank=True)
    demo_url = models.CharField(max_length=256, verbose_name="示例地址", blank=True)
    user = models.ForeignKey(Account, verbose_name="作者", on_delete=models.DO_NOTHING)
    remark = models.CharField(max_length=256, verbose_name="备注", blank=True)
    category = models.CharField(max_length=64, verbose_name="分类", blank=True)
    framework = models.CharField(max_length=64, verbose_name="技术框架", blank=True)
    recommended = models.BooleanField(default=False, verbose_name="是否是精选")
    status = models.BooleanField(default=True, verbose_name="状态")
    created_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新时间", auto_now=True, db_index=True)

    class Meta:
        verbose_name = "作品"
        verbose_name_plural = "作品"
