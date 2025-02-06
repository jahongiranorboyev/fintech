from django.urls import path

from apps.mentors.views import MentorListAPIView

urlpatterns = [
    path('', MentorListAPIView.as_view(), name='mentor-list'),
]
