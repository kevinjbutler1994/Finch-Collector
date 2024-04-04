from rest_framework import serializers
from .models import Finch, Toy, Feeding


class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model= Toy
        field = '__all__'

class FeedingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Feeding
    fields = '__all__'
    read_only_fields = ('finch',)


class FinchSerializer(serializers.ModelSerializer):
  fed_for_today = serializers.SerializerMethodField()
  toys = ToySerializer(many=True, read_only=True) #add this line

  class Meta:
    model = Finch
    fields = '__all__'

  def get_fed_for_today(self, obj):
    return obj.fed_for_today()

