from rest_framework.generics import ListAPIView

from apps.blogs.models import Blog
from apps.blogs.serializers import BlogSerializer


class BlogListAPIView(ListAPIView):
        queryset = Blog.objects.all()
        serializer_class = BlogSerializer