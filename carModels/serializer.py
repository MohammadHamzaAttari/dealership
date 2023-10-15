from rest_framework import serializers
from .models import CarModels

class CarModelsListSerializer(serializers.ModelSerializer):
    model_poster = serializers.ReadOnlyField(source='model_poster.username')
    model_created=serializers.ReadOnlyField()
    class Meta:
        model=CarModels
        fields=['id','model_name','model_created','model_poster','price']
class CarModelsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=CarModels
        fields=['id','model_name','price','description','model_created','model_poster','model_image','car_company','car_trim','car_type']

class CarModelsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=CarModels
        fields=['id','model_name','price','description','model_created','model_poster','model_image','car_company','car_trim','car_type']       