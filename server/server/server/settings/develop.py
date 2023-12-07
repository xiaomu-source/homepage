from .base import * # NOQA

DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'homepage_dev', # 数据库名
        'USER':'root', # 你设置的用户名 - 非root用户
        'PASSWORD':'12345678', # # 换成你自己密码
        'HOST': 'db', # 注意：这里使用的是db别名，docker会自动解析成ip
        'PORT':'3306', # 端口
    }
}
# 设置redis缓存。这里密码为redis.conf里设置的密码
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1", #这里直接使用redis别名作为host ip地址
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "12345678", # 换成你自己密码
        },
    }
}
SWAGGER = False

HOST = f"www.askmedo.cn:3090"
ALLOWED_HOSTS = ['43.138.64.251', 'askmedo.cn', 'www.askmedo.cn']