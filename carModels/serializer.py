from rest_framework import serializers
from .models import CarModels

class CarModelsListSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='model_poster.username')
    model_created=serializers.ReadOnlyField()
    class Meta:
        model=CarModels
        fields=['id','model_name','model_created','user','price']
class CarModelsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=CarModels
        fields=['id','model_name','price','description','model_created','user','model_image','car_company','car_trim','car_type']

class CarModelsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=CarModels
        fields=['id','model_name','price','description','model_created','user','model_image','car_company','car_trim','car_type']       