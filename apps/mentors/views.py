from rest_framework.generics import ListAPIView

from apps.mentors.models import Mentor
from apps.mentors.serializers import MentorListSerializer


class MentorListAPIView(ListAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorListSerializer
