from rest_framework import serializers
from .models import Companies

class CompaniesListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Companies
        fields=['id','company_name','city']
class CompaniesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Companies
        fields=['id','company_name','city','zip_code','website','phone_number','description','logo_image']

class CompaniesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Companies
        fields=['id','company_name','city','zip_code','website','phone_number','description','logo_image']        