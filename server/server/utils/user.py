import bcrypt
import requests
import hashlib

from system.models import Account
from system.serializers import AccountSerializer
from django.contrib.auth.hashers import make_password as _make_password, check_password as _check_password


def random_number(length):
    import random
    possible = "123456789"
    text = ''.join(random.choice(possible) if i > 0 else possible[random.randint(1, len(possible) - 1)] for i in range(length))
    return int(text)

def make_password(value):
    return _make_password(value)

def check_password(value, en_value):
    return _check_password(value, en_value)

def get_browser(request):
    user_agent = request.META.get("HTTP_USER_AGENT")
    if user_agent:
        browsers = [user_agent for user_agent in user_agent.split(" ") if "/" in user_agent]
        if browsers and len(browsers) > 2:
            return browsers[-2]
        if browsers:
            return browsers[0]
    return "未知"

def get_public_ip(request):
    headers = request.headers
    if 'x-real-ip' in headers:
        return headers['x-real-ip']
    if 'x-forwarded-for' in headers:
        ip_list = headers['x-forwarded-for'].split(',')
        return ip_list[0]
    return '0.0.0.0'

def parse_ip(client_ip):
    try:
        response = requests.get(f"https://opendata.baidu.com/api.php?query=[{client_ip}]&co=&resource_id=6006&oe=utf8")
        data = response.json()
        if not data.get('status'):
            return data['data'][0]['location'] if len(data['data']) else '-'
    except Exception as e:
        return "-"

def get_email_avatar(email):
    if email.endswith('@qq.com'):
        return f"https://q1.qlogo.cn/g?b=qq&nk={email}&s=100"
    elif '@' in email and '.' in email:
        hash = hashlib.md5(email.lower().encode('utf-8')).hexdigest()
        return f"https://gravatar.kuibu.net/avatar/{hash}?s=100"
    elif email.endswith('@163.com'):
        user = email.split('@')[0]
        return f"https://mail.163.com/js6/s?func=mbox:getMessageList&sid=zhaohui_hedahua92&r={random_number(10)}&fid=1&user={user}&l=100"
    elif email.endswith('@sina.cn'):
        user = email.split('@')[0]
        return f"http://my.sina.com.cn/avatar.php?uid={user}&size=big"
    else:
        return 'https://mpay.blogcloud.cn/static/admin/images/avatar.jpg'

def get_user_info(user: Account) -> list[dict]:
    # list 是因为 v1 前端需要的 list
    return [AccountSerializer(user).data]