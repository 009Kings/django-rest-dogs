from django.urls import path
from . import views

urlpatterns = [
  path('dogs/', views.dogs_index, name='dogs_index'),
  path('dogs/<int:pk>/', views.dog_detail, name='dog_detail')
]