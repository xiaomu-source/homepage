from rest_framework import serializers
from .models import Code

class CodeSerializer(serializers.ModelSerializer):
    _id = serializers.CharField(source="id")
    createdAt = serializers.DateTimeField(source="created_at")
    updatedAt = serializers.DateTimeField(source="updated_at")
    class Meta:
        model = Code
        fields = ["_id", "name", "type", "url", "remark", "createdAt", "updatedAt",]
