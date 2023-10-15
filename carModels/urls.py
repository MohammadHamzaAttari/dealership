from django.urls import path
from . import views

urlpatterns = [
    path('get/',views.ModelsListAPIView.as_view(),name='Models_list'),
    path('get/<int:id>/',views.ModelsRetrieveAPIView.as_view(),name='Models_Detail'),
    path('create/',views.ModelsCreateAPIView.as_view(),name='Models_create'),
    path('update/<int:id>',views.ModelsRetrieveUpdateAPIView.as_view(),name='Models_update'),
    path('delete/<int:id>',views.ModelsDestroyAPIView.as_view(),name='Models_delete'),
]
