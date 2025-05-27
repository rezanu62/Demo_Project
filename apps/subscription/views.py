from rest_framework import viewsets
from .models import Subcription
from .serializers import SubcriptionSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
import stripe
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

class SubcriptionViewSet(viewsets.ModelViewSet):
    queryset = Subcription.objects.all()
    serializer_class = SubcriptionSerializer

# Initialize Stripe with secret key
class CreateCheckoutSessionView(APIView):
    def post(self, request):
        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': 1000,  # $10.00
                        'product_data': {
                            'name': 'Pro Subscription',
                        },
                    },
                    'quantity': 1,
                }],
                mode='payment',  # or 'subscription'
                success_url='http://localhost:8000/success/',
                cancel_url='http://localhost:8000/cancel/',
                customer_email='test@example.com',  # Optional
            )
            return Response({'checkout_url': checkout_session.url})
        except Exception as e:
            return Response({'error': str(e)}, status=400)
# Set your Stripe secret key
stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET  # you'll get this from Stripe

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    #Handle specific events
    if event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        # Fulfill the purchase, mark order as paid etc.
        print("PaymentIntent was successful:", payment_intent['id'])

    elif event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        # Fulfill order, save transaction, etc.
        print("Checkout session completed:", session['id'])

    return HttpResponse(status=200)