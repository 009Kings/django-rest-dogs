from django.shortcuts import render
from django.http import HttpResponse
from .models import Dog
from .serializers import DogSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# # Create your views here.
@api_view(['GET', 'POST'])
def dogs_index(request):
  if request.method == 'GET':
    dogs = Dog.objects.all()
    serializer = DogSerializer(dogs, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = DogSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET', 'DELETE'])
def dog_detail(request, pk):
  dog = Dog.objects.get(pk=pk)
  if request.method == 'GET':
    serializer = DogSerializer(dog)
    return Response(serializer.data, status=status.HTTP_200_OK)
  elif request.method == 'DELETE':
    print("in here")
    dog.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
