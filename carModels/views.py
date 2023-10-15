from django.shortcuts import render
from rest_framework import generics,permissions
from .models import CarModels
from .serializer import CarModelsListSerializer,CarModelsDetailSerializer
# Create your views here.
class ModelsListAPIView(generics.ListAPIView):
    queryset=CarModels.objects.all()
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=CarModelsListSerializer
    
    def get_quertset(self):
        user=self.request.user
        return CarModels.objects.filter(model_poster=user).order_by('-model_created')
    
class ModelsRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field='id'
    queryset=CarModels.objects.all()    
    serializer_class=CarModelsDetailSerializer
    
class ModelsCreateAPIView(generics.CreateAPIView):
    queryset=CarModels.objects.all()
    serializer_class=CarModelsDetailSerializer
    
class ModelsRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field='id'
    queryset=CarModels.objects.all()        
    serializer_class=CarModelsDetailSerializer

class ModelsDestroyAPIView(generics.DestroyAPIView):
    lookup_field='id'
    queryset=CarModels.objects.all()        