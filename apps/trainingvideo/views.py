from rest_framework import viewsets
from .models import TrainingVideo, FAQ
from .serializers import TrainingVideoSerializer, FAQSerializer

class TrainingVideoViewSet(viewsets.ModelViewSet):
    queryset = TrainingVideo.objects.all()
    serializer_class = TrainingVideoSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    