
#user
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import CustomUser
from .serializers import CustomUserSerializer

#UserFuntion
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]  # or [IsAdminUser] if only staff should access




#Logout
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

#LogoutViewFuntion
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated] 
    
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Successfully logged out."}, status = status.HTTP_205_RESET_CONTENT)
        except KeyError:
            return Response({"error" : "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)
        except TokenError:
            return Response({"error" : "Invalid token"}, status= status.HTTP_400_BAD_REQUEST)


#PasswordReset
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

User = get_user_model()

class PasswordResetView(APIView):
    def post(self, request): 
        email = request.data.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            reset_url = f"http://localhost:8000/api/password-reset-confirm/{uid}/{token}"
            send_mail(
                'Password Reset Request',
                f'Click the link below to reset your password:\n{reset_url}',
                'sawafrafa003@gmail.com',
                [user.email],
                fail_silently=False,
            )
        return Response({'detail' : 'Password reset link sent if email exists.'}, status=status.HTTP_200_OK)





#PasswordResetConfirm
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model



UserModel = get_user_model()

class PassswordResetConfirmView(APIView):
    def post(self, request, uidb64, token):
        password = request.data.get('password')

        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = UserModel.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            user = None

        if user and default_token_generator.check_token(user, token):
            user.set_password(password)
            user.save()
            return Response({'detail' : 'Password has been reset successfully.'}, status = status.HTTP_200_OK)
        
        return Response ({'error' : 'Invalid token or user ID'}, status=status.HTTP_400_BAD_REQUEST)



