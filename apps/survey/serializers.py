from rest_framework import serializers
from .models import Survey, Option, SurveyUser

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'
        
class SurveyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyUser
        fields = '__all__'

class SurveySerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)
    user = SurveyUserSerializer(read_only=True)

    class Meta:
        model = Survey
        fields = '__all__'
