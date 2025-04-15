from rest_framework import serializers
from .models import Chair, Sofa, DiningSet

class ChairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chair
        fields = '__all__'

class SofaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sofa
        fields = '__all__'

class DiningSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiningSet
        fields = '__all__'
