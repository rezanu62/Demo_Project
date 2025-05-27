from django.urls import path
from .views import CreateCheckoutSessionView, CreateStripePortalSessionView
from .views import stripe_webhook

urlpatterns = [
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('payment/webhook/', stripe_webhook, name='stripe-webhook'),
    path('create-portal-session/', CreateStripePortalSessionView.as_view(), name='create-portal-session'),
    
]