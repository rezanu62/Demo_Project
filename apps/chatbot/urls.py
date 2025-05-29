from django.urls import path
from .views import track_queries_view, chatbot_api

urlpatterns = [
    path('api/chat/', chatbot_api, name='chatbot-api'),
    path('tracked/', track_queries_view, name='tracked_view'),
]
