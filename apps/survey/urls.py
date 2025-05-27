from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OptionViewSet, SurveyUserViewSet, SurveyViewSet

urlpatterns = [
    path('option/', OptionViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy', 'put': 'update'}), name='option-list'),
    path('survey/', SurveyUserViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy', 'put': 'update'}), name='survey-list'),
    path('survey/<int:pk>/', SurveyViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy', 'put': 'update'}), name='survey-detail'),
     
]

