from rest_framework import serializers
from .models import Subcription

class SubcriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcription
        fields = '__all__'