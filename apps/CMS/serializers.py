from rest_framework import serializers
from .models import Cards, Landing_page, About_us, CMS


class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = '__all__'


class LandingPageSerializer(serializers.ModelSerializer):
    card_id = CardsSerializer(read_only=True)

    class Meta:
        model = Landing_page
        fields = '__all__'


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = About_us
        fields = '__all__'


class CMSSerializer(serializers.ModelSerializer):
    #landing_page_id = LandingPageSerializer(read_only=True)
    #about_us_id = AboutUsSerializer(read_only=True)

    class Meta:
        model = CMS
        fields = '__all__'
