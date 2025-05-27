from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import SubcriptionViewSet
from .views import CreateCheckoutSessionView
from . import views


urlpatterns = [
    path('subscription/', SubcriptionViewSet.as_view({'get': 'list', 'post': 'create'}), name='Subscription'),
    path('create-subscription-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    # path('stripe/webhook/', views.stripe_webhook, name='stripe-webhook'),
]
