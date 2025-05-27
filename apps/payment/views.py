from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import stripe
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from .models import StripeCustomer


stripe.api_key = settings.STRIPE_SECRET_KEY

# For One time payment
# class CreateCheckoutSessionView(APIView):
#     def post(self, request):
#         try:
#             checkout_session = stripe.checkout.Session.create(
#                 payment_method_types=['card'],
#                 line_items=[{
#                     'price_data': {
#                         'currency': 'usd',
#                         'unit_amount': 1000,  # $10.00
#                         'product_data': {
#                             'name': 'Pro Subscription',
#                         },
#                     },
#                     'quantity': 1,
#                 }],
#                 mode='payment',  # or 'subscription'
#                 success_url='http://localhost:8000/success/',
#                 cancel_url='http://localhost:8000/cancel/',
#                 customer_email='test@example.com',  # Optional
#             )
#             return Response({'checkout_url': checkout_session.url})
#         except Exception as e:
#             return Response({'error': str(e)}, status=400)


# For subcription        

class CreateCheckoutSessionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        sc, created = StripeCustomer.objects.get_or_create(user=user)
        if not sc.stripe_customer_id:
            stripe_customer = stripe.Customer.create(email=user.email)
            sc.stripe_customer_id = stripe_customer.id
            sc.save()
        try:
            checkout_session = stripe.checkout.Session.create(
                customer=sc.stripe_customer_id,
                payment_method_types=['card'],
                line_items=[{
                    'price': 'price_1RTFXrH8n0QbNY3cF8DVJLW8',
                    'quantity': 1,
                }],
                mode='subscription',  # or 'subscription'
                success_url='http://localhost:8000/success/',
                cancel_url='http://localhost:8000/cancel/',
            )
            return Response({'checkout_url': checkout_session.url})
        except Exception as e:
            return Response({'error': str(e)}, status=400)
        

# views.py


# @csrf_exempt
# def stripe_webhook(request):
#     payload = request.body
#     sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
#     event = None

#     try:
#         event = stripe.Webhook.construct_event(
#             payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
#         )
#     except ValueError:
#         return HttpResponse(status=400)
#     except stripe.error.SignatureVerificationError:
#         return HttpResponse(status=400)

#     data = event['data']['object']

#     if event['type'] in ['customer.subscription.created', 'customer.subscription.updated']:
#         subscription = data
#         sc = StripeCustomer.objects.filter(stripe_customer_id=subscription['customer']).first()
#         if sc:
#             sc.stripe_subscription_id = subscription['id']
#             sc.subscription_status = subscription['status']
#             sc.save()

#     elif event['type'] == 'customer.subscription.deleted':
#         sc = StripeCustomer.objects.filter(stripe_customer_id=data['customer']).first()
#         if sc:
#             sc.subscription_status = 'inactive'
#             sc.save()


#     return HttpResponse(status=200)


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except Exception:
        return HttpResponse(status=400)

    data = event['data']['object']

    if event['type'] in ['customer.subscription.created', 'customer.subscription.updated']:
        customer_id = data.get('customer')
        subscription_id = data.get('id')
        status = data.get('status')

        sc = StripeCustomer.objects.filter(stripe_customer_id=customer_id).first()
        if sc:
            sc.stripe_subscription_id = subscription_id
            sc.subscription_status = status
            sc.save()

    elif event['type'] == 'customer.subscription.deleted':
        customer_id = data.get('customer')
        sc = StripeCustomer.objects.filter(stripe_customer_id=customer_id).first()
        if sc:
            sc.subscription_status = 'inactive'
            sc.save()

    elif event['type'] == 'invoice.payment_succeeded':
        customer_id = data.get('customer')
        sc = StripeCustomer.objects.filter(stripe_customer_id=customer_id).first()
        if sc:
            # Mark subscription active when payment succeeds
            sc.subscription_status = 'active'
            sc.save()

    return HttpResponse(status=200)


class CreateStripePortalSessionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        try:
            sc = StripeCustomer.objects.get(user=user)
        except StripeCustomer.DoesNotExist:
            return Response({'error': 'Stripe customer not found'}, status=404)

        try:
            session = stripe.billing_portal.Session.create(
                customer=sc.stripe_customer_id,
                return_url='http://localhost:8000/dashboard/',  # Replace with your actual return URL
            )
            return Response({'portal_url': session.url})
        except Exception as e:
            return Response({'error': str(e)}, status=400)