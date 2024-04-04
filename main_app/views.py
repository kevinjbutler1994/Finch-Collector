# additional imports below
from rest_framework import generics
from .models import Finch, Feeding, Toy
from .serializers import FinchSerializer, FeedingSerializer, ToySerializer
from rest_framework.decorators import APIView

class Home(generics.ListCreateAPIView):
  queryset = Finch.objects.all()
  serializer_class = FinchSerializer

class FinchList(generics.ListCreateAPIView):
  queryset = Finch.objects.all()
  serializer_class = FinchSerializer

class FinchDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Finch.objects.all()
  serializer_class = FinchSerializer
  lookup_field = 'id'

  # add (override) the retrieve method below
  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)

    # Get the list of toys not associated with this cat
    toys_not_associated = Toy.objects.exclude(id__in=instance.toys.all())
    toys_serializer = ToySerializer(toys_not_associated, many=True)

    return ({
        'finch': serializer.data,
        'toys_not_associated': toys_serializer.data
    })


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

class ToyList(generics.ListCreateAPIView):
  queryset = Toy.objects.all()
  serializer_class=ToySerializer()

class ToyDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Toy.objects.all()
  serializer_class = ToySerializer
  
class AddToyToFinch(APIView):
  def post(self, request, finch_id, toy_id):
    finch = Finch.objects.get(id=finch_id)
    toy = Toy.objects.get(id=toy_id)
    finch.toys.add(toy)
    return ({'message': f'Toy {toy.name} added to Finch {finch.name}'})
