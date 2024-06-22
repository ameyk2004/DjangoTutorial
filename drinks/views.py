from django.shortcuts import render
from django.http import JsonResponse
from . serializers import DrinkSerializer
from . models import Drinks

# Create your views here.
def drink_list(request):
    drinks = Drinks.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    return JsonResponse(serializer.data, safe=False)