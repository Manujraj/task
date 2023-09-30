from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def drink_list(request, format=None):

    if request.method == 'GET':
        drinks = Drink.objects.all()
        Serializer = DrinkSerializer(drinks, many=True)
        return Response(Serializer.data)
    
    if request.method == 'POST':
        Serializer = DrinkSerializer(data=request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None):

    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        Serializer = DrinkSerializer(drink)
        return Response(Serializer.data)
    
    elif request.method == 'PUT':
        Serializer = DrinkSerializer(drink, data=request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data)
        return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)