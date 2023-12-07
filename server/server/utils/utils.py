from datetime import datetime, timedelta

import jwt
from django.db import models
from django.db.models import QuerySet, Q
from rest_framework import serializers
from rest_framework.routers import SimpleRouter

from server.settings.base import SIGN_KEY


def get_jwt_token(data: dict, sign_key: str = SIGN_KEY) -> str:
    """生成 jwt"""
    expiration_time = datetime.now() + timedelta(days=3) # 过期时间设置为三天
    payload = {
        **data,
        "exp": expiration_time,
    }
    token = jwt.encode(payload, sign_key, algorithm='HS256')
    return f"Bearer {token}"

def register(router: SimpleRouter, view_sets: list[tuple]) -> None:
    """routers register"""
    for name, view_set in view_sets:
        router.register(name, view_set, name)

def dict_remove_empty_key(data: dict) -> dict:
    for key, value in data.copy().items():
        if not value:
            data.pop(key)
    return data

def slice_array(query: QuerySet | list, offset: int | None, limit: int | None) -> QuerySet | list:
    """截取查询结果"""
    if offset is not None and limit is None:
        query = query[limit:]
    elif offset is None and limit is not None:
        query = query[:limit]
    elif offset is not None and limit is not None:
        query = query[offset : offset + limit]
    return query

def filter_queryset_by_partial_match(model: models, params: dict) -> QuerySet:
    query = Q()
    if not params:
        return model.objects.all()
    for key, value in params.items():
        lookup = f"{key}__icontains"
        query |= Q(**{lookup: value})
    queryset = model.objects.filter(query)
    return queryset

def get_list_view_data(model: models, serializer: serializers, validated_data: dict):
    model_objs = filter_queryset_by_partial_match(model, validated_data.get("params"))
    if order_by_filed := validated_data.get("order_by_field"):
        model_objs = model_objs.order_by(order_by_filed)

    current = validated_data.get("current") or 1
    page_size = validated_data.get("page_size") or 15
    if current is None or page_size is None:
        raise Exception("offset is None or limit is None")
    offset = (current - 1) * page_size

    return {
        "result": serializer(slice_array(model_objs, offset, page_size), many=True).data,
        'current': validated_data.get("current"),
        'pageSize': validated_data.get("page_size"),
        'total': model_objs.count(),
    }
