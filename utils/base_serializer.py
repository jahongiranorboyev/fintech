from rest_framework.serializers import ModelSerializer
from .base_model import AbstractBaseModel


class BaseSerializer(ModelSerializer):
    class Meta:
        model = AbstractBaseModel
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
