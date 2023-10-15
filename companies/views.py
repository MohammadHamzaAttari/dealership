from django.shortcuts import render
from rest_framework import generics
from .models import Companies
from .serializers import CompaniesListSerializer,CompaniesDetailSerializer

# Create your views here.
class CompaniesListAPIView(generics.ListAPIView):
    queryset=Companies.objects.all()
    serializer_class=CompaniesListSerializer
    
class CompaniesRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field='id'
    queryset=Companies.objects.all()
    serializer_class=CompaniesDetailSerializer   

class CompaniesCreateAPIView(generics.CreateAPIView):
    queryset=Companies.objects.all()
    serializer_class=CompaniesDetailSerializer    

class CompaniesRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field='id'
    queryset=Companies.objects.all()
    serializer_class=CompaniesDetailSerializer    
class CompaniesDestroyAPIView(generics.DestroyAPIView):
    lookup_field='id'
    queryset=Companies.objects.all()    