# additional imports below
from rest_framework import generics
from .models import Finch, Feeding
from .serializers import FinchSerializer, FeedingSerializer

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

class FeedingListCreate(generics.ListCreateAPIView):
  serializer_class = FeedingSerializer

  def get_queryset(self):
    finch_id = self.kwargs['finch_id']
    return Feeding.objects.filter(finch_id=finch_id)

  def perform_create(self, serializer):
    finch_id = self.kwargs['finch_id']
    finch = Finch.objects.get(id=finch_id)
    serializer.save(finch=finch)

class FeedingDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = FeedingSerializer
  lookup_field = 'id'

  def get_queryset(self):
    finch_id = self.kwargs['finch_id']
    return Feeding.objects.filter(finch_id=finch_id)
