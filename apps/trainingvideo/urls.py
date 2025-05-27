from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TrainingVideoViewSet, FAQViewSet

urlpatterns = [
    path('videos/', TrainingVideoViewSet.as_view({'get': 'list', 'post': 'create'}), name='Training-Video'),
    path('faq/', FAQViewSet.as_view({'get': 'list', 'post': 'create'}), name='FAQ'),
]