# additional imports below
from rest_framework import generics
from .models import Finch
from .serializers import FinchSerializer

class FinchList(generics.ListCreateAPIView):
  queryset = Finch.objects.all()
  serializer_class = FinchSerializer

class FinchDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Finch.objects.all()
  serializer_class = FinchSerializer
  lookup_field = 'id'

class Home(generics.ListCreateAPIView):
  queryset = Finch.objects.all()
  serializer_class = FinchSerializer
