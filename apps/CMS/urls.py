from .views import CardsViewSet, LandingPageViewSet, AboutUsViewSet, CMSViewSet
from django.urls import path

urlpatterns = [
    
    path('card/', CardsViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy', 'put': 'update'}), name='card'),
    path('landing-page/', LandingPageViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy', 'put': 'update'}), name='card-list'),
    path('about-us/', AboutUsViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy', 'put': 'update'}), name='about-us'),
    path('cms/', CMSViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy', 'put': 'update'}), name='cms-list'),
]

