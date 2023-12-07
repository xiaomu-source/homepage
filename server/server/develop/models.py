from django.db import models

class Code(models.Model):
    name = models.CharField(max_length=64, verbose_name="文件名称")
    type = models.CharField(max_length=64, verbose_name="文件类型")
    url = models.CharField(max_length=256, verbose_name="下载地址")
    remark = models.CharField(max_length=256, verbose_name="备注")
    created_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新时间", auto_now=True, db_index=True)