import re
from enum import Enum

from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator as _EmailValidator
from rest_framework import serializers


def is_email(email: str = None) -> bool:
    if not email:
        return False
    email_validator = _EmailValidator()
    result = True
    try:
        email_validator(email)
    except ValidationError:
        result = False
    return result


REGEX_PHONE = re.compile(r"1\d{10}")


def is_phone(phone: str = None) -> bool:
    if not phone:
        return False
    return bool(REGEX_PHONE.fullmatch(phone))


def is_valid_username(data):
    """是否为合法的用户名"""
    return isinstance(data, str) and data and "@" not in data and not data.isdigit()


# ----------------------- 上面是验证函数 -----------------------


# ----------------------- 下面是 Serializers - Fields -----------------------


class BoolField(serializers.BooleanField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class StrField(serializers.CharField):
    """针对我们内部设定做过优化的字符串字段"""

    def __init__(self, **kwargs):
        kwargs.setdefault("allow_blank", True)
        super().__init__(**kwargs)


class UUIDField(serializers.UUIDField):
    """我们用到的 UUID 都是经过 hex 转换的"""

    def to_internal_value(self, data):
        return super().to_internal_value(data).hex


class BooleanNullField(serializers.BooleanField):
    """我们用到的有些布尔序列化，会把 null 视为 False"""

    NULL_VALUES = {}
    FALSE_VALUES = {
        "f",
        "F",
        "n",
        "N",
        "no",
        "No",
        "NO",
        "false",
        "False",
        "FALSE",
        "off",
        "Off",
        "OFF",
        "0",
        0,
        0.0,
        "null",
        "Null",
        "NULL",
        "",
        None,
        False,
    }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("allow_null", True)
        super().__init__(*args, **kwargs)


class CommaListField(serializers.ListField):
    """针对 GET 请求优化过的 ListField

    DRF 默认的 ListSerializer 只支持 GET /path/?type=1&type=2&type=3 的调用方式
    我们额外支持了 GET /path/?type=1,2,3 这样的调用方式
    """

    def to_internal_value(self, data):
        if isinstance(data, str):
            data = data.split(",")
        return super().to_internal_value(data)


class EnumField(serializers.ChoiceField):
    """枚举值"""

    def __init__(self, enum: type[Enum], **kwargs):
        super().__init__(choices=enum.choices(), **kwargs)


class UsernameField(serializers.CharField):
    """验证用户名"""

    default_error_messages = {"invalid_username": "invalid username"}

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        if data and ("@" in data or data.isdigit()):
            self.fail("invalid_username")
        return data


class PhoneField(serializers.CharField):
    """手机号"""

    default_error_messages = {"invalid_phone": "手机号不正确"}

    def to_internal_value(self, data):
        # 长度为 0 的字符串认为是 None
        if isinstance(data, str) and not len(data.strip()):
            data = None
        data = super().to_internal_value(data)
        if data and not is_phone(data):
            self.fail("invalid_phone")
        return data


class EmailField(serializers.CharField):
    """邮箱"""

    default_error_messages = {"invalid_email": "邮箱不正确"}

    def to_internal_value(self, data):
        # 长度为 0 的认为是 None
        if isinstance(data, str) and not len(data.strip()):
            data = None
        data = super().to_internal_value(data)
        if data and not is_email(data):
            self.fail("invalid_email")
        return data
