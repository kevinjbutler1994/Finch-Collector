from rest_framework import serializers
from .models import Finch

class FinchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finch
        fields = '__all__'
