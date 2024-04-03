from rest_framework import serializers
from .models import Finch
from .models import Feeding

class FinchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finch
        fields = '__all__'


class FeedingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Feeding
    fields = '__all__'
    read_only_fields = ('finch',)
