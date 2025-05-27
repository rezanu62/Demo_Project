from rest_framework import viewsets
from .models import Option, SurveyUser, Survey
from .serializers import OptionSerializer, SurveyUserSerializer, SurveySerializer

class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

class SurveyUserViewSet(viewsets.ModelViewSet):
    queryset = SurveyUser.objects.all()
    serializer_class = SurveyUserSerializer

class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer



