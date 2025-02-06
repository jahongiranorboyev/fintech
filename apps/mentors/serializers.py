from apps.mentors.models import Mentor
from utils.base_serializer import BaseSerializer


class MentorListSerializer(BaseSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'
