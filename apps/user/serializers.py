from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'company_name',
            'job_title',
            'is_staff',
            'is_active',
            'date_joined'
        ]
        read_only_fields = ('is_staff', 'is_active', 'date_joined')