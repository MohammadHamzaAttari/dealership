from django.urls import path
from . import views

urlpatterns = [
    path('get/',views.CompaniesListAPIView.as_view(),name='companies_list'),
    path('get/<int:id>/',views.CompaniesRetrieveAPIView.as_view(),name='companies_Detail'),
    path('create/',views.CompaniesCreateAPIView.as_view(),name='companies_create'),
    path('update/<int:id>',views.CompaniesRetrieveUpdateAPIView.as_view(),name='companies_update'),
    path('delete/<int:id>',views.CompaniesDestroyAPIView.as_view(),name='companies_delete'),
]

