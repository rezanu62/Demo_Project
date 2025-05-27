from rest_framework import viewsets
# from rest_framework.views import APIView
# from rest_framework.response import Response
from .models import Cards, Landing_page, About_us, CMS
from .serializers import CardsSerializer, LandingPageSerializer, AboutUsSerializer, CMSSerializer

class CardsViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = Cards.objects.all()
    serializer_class = CardsSerializer


class LandingPageViewSet(viewsets.ModelViewSet):
    queryset = Landing_page.objects.all()
    serializer_class = LandingPageSerializer


class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = About_us.objects.all()
    serializer_class = AboutUsSerializer


class CMSViewSet(viewsets.ModelViewSet):
    queryset = CMS.objects.all()
    serializer_class = CMSSerializer


# class CardListView(APIView):
#     permission_classes = []

    # def get(self, request):
    #     cms = Cards.objects.all()
    #     serializer = CardsSerializer(cms, many=True)
    #     return Response(serializer.data)
    
    # def post(self, request):
    #     serializer = CardsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)
    

    
    # def put(self, request):
    #     cms = Cards.objects.all()
    #     serializer = CardsSerializer(cms, many=True)
    #     return Response(serializer.data)
    
    # def delete(self, request):
    #     serializer = CardsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)