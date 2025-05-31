from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, LogoutView, PasswordResetView, PassswordResetConfirmView

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')

urlpatterns = [
    #user
    path('', include(router.urls)),

    #Logout
    path('logout/', LogoutView.as_view(), name = 'logout'),
    
    #Password reset
    path('password-reset/', PasswordResetView.as_view(), name = 'password-reset'),

    #Password confirm
    path('password-reset-confirm/<uidb64>/<token>/', PassswordResetConfirmView.as_view(), name='password-reset-confirm')

]