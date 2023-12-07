import functools
from typing import Callable

import inflection
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.request import Request
from rest_framework import serializers

from system.models import UserOptLog, Permission, Role
from utils.authentications import AccountViewSet
from utils.response import BadResponse
from utils.user import get_public_ip, parse_ip, get_browser


def action_record(module: str, content:str = None):
    def decorate(fuc):
        @functools.wraps(fuc)
        def wrapper(view, request, **kwargs):
            client_ip = get_public_ip(request)
            browser = get_browser(request)
            address = parse_ip(client_ip)
            data = {
                "operator": request.user.nickname or request.user.username or "未知",
                "operator_id": request.user.id,
                "module": module,
                "platform": browser,
                "operator_ip": client_ip,
                "address": address or "-",
                "content": content or request.META.get("PATH_INFO")
            }
            UserOptLog.objects.create(**data)
            return fuc(view, request, **kwargs)
        return wrapper
    return decorate

def wrap_swagger(func: Callable, definition: type, response_siri) -> Callable:
    """利用我们定义的校验，给函数补上对应的 swagger_auto_schema
    - 对于 GET / POST,PUT,PATCH, 我们校验的分别是 params / body, 所以函数里要做额外的判断
    https://drf-yasg.readthedocs.io/en/stable/custom_spec.html
    """
    doc_string = (func.__doc__ or "").strip() + "\n"
    summary, description = doc_string.split("\n", 1)
    query_serializer = None
    request_body = None
    # 此处需要判断 func 是验证 params 还是 request_body, 所以根据函数名或者 @actions 的参数来判断
    if func.__name__ in ("list", "get", "retrieve") or "get" in getattr(func, "mapping", {}):
        query_serializer = definition
    else:
        request_body = definition
    responses = {200: ""}
    if response_siri:
        responses = {200: openapi.Response((response_siri.__doc__ or "").strip(), schema=response_siri)}
    swagger_schema = swagger_auto_schema(
        operation_description=description,
        operation_summary=summary,
        responses=responses,
        query_serializer=query_serializer,
        request_body=request_body,
    )
    return swagger_schema(func)

def _set_id_field(validated_data: dict) -> dict:
    validated_data["id"] = int(validated_data.get("_id") or validated_data.get("id"))
    validated_data.pop("_id")
    return validated_data

def _set_filter_field(validated_data: dict) -> dict:
    params = validated_data.get("params") or {}
    validated_data["params"] = {inflection.underscore(key): value for key, value in params.items() if value}
    return validated_data

def _set_pagination_field(validated_data: dict) -> dict:
    pagination = validated_data.get("pagination") or {}
    validated_data["current"] = int(pagination.get("current")) or 1
    validated_data["page_size"] = int(pagination.get("pageSize")) or 15
    validated_data["total"] = pagination.get("total") or 0
    validated_data["hide_on_single_page"] = pagination.get("hideOnSinglePage") or True
    return validated_data

def _set_order_field(validated_data: dict) -> dict:
    sort = validated_data.get("sort") or {}
    validated_data["column_key"] = (column_key := inflection.underscore(sort.get("columnKey") or "createdAt"))
    validated_data["order"] = (order := "-" if sort.get("order") == "descend" else "")
    validated_data["order_by_field"] = f"{order}{column_key}"
    return validated_data

def _under_sore_key(validated_data: dict) -> dict:
    return {inflection.underscore(key): value for key, value in validated_data.items() if value}

def schema_required(
    response_siri=None,
    siri: type[serializers.Serializer] | None = None,
    /,
    with_list: bool = False,
    with_id: bool = False,
    under_sore: bool = False, # 前端传key遵循驼峰风格， 后端遵循下划线风格，设置为 True 可以把createdAt 转成 created_at
    **fields,
):
    """指定输入的参数跟返回的参数

    样例：
    @decorator.schema_required(QuestionSiri)
    def some_api_method(self, request):
        pass

    @decorator.schema_required(offset=serializers.IntegerField(), limit=serializers.IntegerField())
    def other_api_method(self, request):
        pass
    """
    if not siri:
        siri = serializers.Serializer
    # 带有列表的字段
    if with_list:
        fields.update(
            params = serializers.DictField(required=False, help_text="过滤字段"),
            pagination = serializers.DictField(required=False, help_text="分页字段"),
            sort = serializers.DictField(required=False, help_text="排序字段"),
        )
    if with_id:
        fields.update(
            _id = serializers.CharField(required=True, help_text="id")
        )

    def decorator(func):
        name = f"Gen.{func.__module__}.{func.__qualname__}.Siri".replace(".", "_")
        siri_class = type(inflection.camelize(name), (siri,), fields)
        func = wrap_swagger(func, siri_class, response_siri)

        @functools.wraps(func)
        def wrapper(view: AccountViewSet, request: Request, **kwargs):
            if request.method in ["POST", "PUT", "PATCH", "DELETE"]:
                data = request.data
            elif request.method in ["GET"]:
                data = dict(request.GET.items())
            else:
                data = {}

            validated_siri: serializers.Serializer = siri_class(data=data)
            validated_siri.is_valid(raise_exception=True)
            validated_data = validated_siri.validated_data
            # 设置 id 字段
            if validated_data.get("_id"):
                validated_data = _set_id_field(validated_data)
            # 设置过滤字段
            if validated_data.get("params"):
                validated_data = _set_filter_field(validated_data)
            # 设置分页字段
            if validated_data.get("pagination"):
                validated_data = _set_pagination_field(validated_data)
            # 设置排序字段
            if validated_data.get("sort"):
                validated_data = _set_order_field(validated_data)
            # 统一前端 key 的命名风格
            if under_sore:
                validated_data = _under_sore_key(validated_data)
            view.validated_data = validated_data
            return func(view, request, **kwargs)

        return wrapper

    return decorator

def check_api_permission(auth = None):
    def decorate(fuc):
        @functools.wraps(fuc)
        def wrapper(view, request, **kwargs):
            try:
                role = Role.objects.get(id=request.user.role.id)
            except Role.DoesNotExist:
                return BadResponse("该用户还未分配角色")
            if not role.status:
                return BadResponse("您的角色已被禁用，请联系管理员")
            if not ('*' in role.perms or auth in role.perms):
                return BadResponse("您暂时没有权限访问，请联系管理员")
            permission = Permission.objects.filter(key=auth).first()
            if not (permission and permission.status):
                return BadResponse("您访问的权限已被禁用，请联系管理员")
            return fuc(view, request, **kwargs)
        return wrapper
    return decorate

def check_user_role(allowed_roles: list[Role]):
    def decorate(fuc):
        @functools.wraps(fuc)
        def wrapper(view, request, **kwargs):
            role = request.user.role
            if not role in allowed_roles:
                return BadResponse("您未被授权访问此资源")
            return fuc(view, request, **kwargs)
        return wrapper
    return decorate

def check_user_permission(allowed_permissions):
    def decorate(fuc):
        @functools.wraps(fuc)
        def wrapper(view, request, **kwargs):
            return fuc(view, request, **kwargs)
        return wrapper
    return decorate

def has_menu_permission(user_roles, men_route):
    def decorate(fuc):
        @functools.wraps(fuc)
        def wrapper(view, request, **kwargs):
            return fuc(view, request, **kwargs)
        return wrapper
    return decorate

def has_button_permission(user_roles, button_route):
    def decorate(fuc):
        @functools.wraps(fuc)
        def wrapper(view, request, **kwargs):
            return fuc(view, request, **kwargs)
        return wrapper
    return decorate
