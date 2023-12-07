# Generated by Django 4.2.7 on 2023-12-07 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=256, verbose_name='留言内容')),
                ('hidden', models.BooleanField(default=False, verbose_name='是否隐藏')),
                ('reply_id', models.IntegerField(blank=True, null=True, verbose_name='关联的回复ID')),
                ('like_num', models.IntegerField(default=0, verbose_name='点赞量')),
                ('oppose_num', models.IntegerField(default=0, verbose_name='反对量')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='更新时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='system.account', verbose_name='关联的用户ID')),
            ],
            options={
                'verbose_name': '留言',
                'verbose_name_plural': '留言',
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=256, verbose_name='原始用户ID')),
                ('to_user', models.CharField(max_length=256, verbose_name='目标用户ID')),
                ('content', models.CharField(max_length=256, verbose_name='回复内容')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='更新时间')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.message', verbose_name='关联的留言ID')),
            ],
            options={
                'verbose_name': '回复',
                'verbose_name_plural': '回复',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='作品名称')),
                ('cover', models.CharField(blank=True, max_length=256, verbose_name='作品封面')),
                ('abstract', models.CharField(max_length=256, verbose_name='作品简介')),
                ('content', models.CharField(max_length=256, verbose_name='作品内容')),
                ('source_url', models.CharField(blank=True, max_length=256, verbose_name='源码地址')),
                ('demo_url', models.CharField(blank=True, max_length=256, verbose_name='示例地址')),
                ('remark', models.CharField(blank=True, max_length=256, verbose_name='备注')),
                ('category', models.CharField(blank=True, max_length=64, verbose_name='分类')),
                ('framework', models.CharField(blank=True, max_length=64, verbose_name='技术框架')),
                ('recommended', models.BooleanField(default=False, verbose_name='是否是精选')),
                ('status', models.BooleanField(default=True, verbose_name='状态')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='更新时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='system.account', verbose_name='作者')),
            ],
            options={
                'verbose_name': '作品',
                'verbose_name_plural': '作品',
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='博文名称')),
                ('cover', models.CharField(blank=True, max_length=256, verbose_name='博文封面')),
                ('abstract', models.CharField(blank=True, max_length=256, verbose_name='博文摘要')),
                ('content', models.TextField(help_text='正文必须为MarkDown格式', verbose_name='博文内容')),
                ('remark', models.CharField(blank=True, max_length=256, verbose_name='备注')),
                ('category', models.CharField(blank=True, max_length=64, verbose_name='分类')),
                ('view_num', models.IntegerField(default=0, verbose_name='浏览量')),
                ('like_num', models.IntegerField(default=0, verbose_name='点赞量')),
                ('is_reship', models.BooleanField(default=False, verbose_name='是否转载')),
                ('is_reship_url', models.CharField(blank=True, max_length=256, null=True, verbose_name='转载文章地址')),
                ('is_reship_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='转载文章名称')),
                ('recommended', models.BooleanField(default=False, verbose_name='是否精选')),
                ('like_token', models.JSONField(blank=True, null=True, verbose_name='点赞的临时标识')),
                ('status', models.BooleanField(default=True, verbose_name='状态 发布和草稿')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='更新时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='system.account', verbose_name='作者')),
            ],
            options={
                'verbose_name': '博客文章',
                'verbose_name_plural': '博客文章',
            },
        ),
    ]
