from django.urls import path
from .views import Home, FinchList, FinchDetail # additional imports

urlpatterns = [
  path('', Home.as_view(), name='home'),
  # new routes below 
  path('finches/', FinchList.as_view(), name='finch-list'),
  path('finches/<int:id>/', FinchDetail.as_view(), name='finch-detail'),
]
