from utils.base_serializer import BaseSerializer
from .models import Blog

class BlogSerializer(BaseSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
