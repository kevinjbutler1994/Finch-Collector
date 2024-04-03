from django.urls import path
from .views import Home, FinchList, FinchDetail, FeedingListCreate, FeedingDetail # additional imports

urlpatterns = [
  path('', Home.as_view(), name='home'),
  # new routes below 
  path('finches/', FinchList.as_view(), name='finch-list'),
  path('finches/<int:id>/', FinchDetail.as_view(), name='finch-detail'),
  path('finches/<int:finch_id>/feedings/', FeedingListCreate.as_view(), name='feeding-list-create'),
	path('finches/<int:finch_id>/feedings/<int:id>/', FeedingDetail.as_view(), name='feeding-detail'),
]


