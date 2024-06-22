from . models import Drinks
from rest_framework import serializers

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drinks
        fields = ['id', 'name', 'description' ]