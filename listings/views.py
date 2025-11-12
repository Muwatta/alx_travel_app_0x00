# listings/views.py
from .models import Listing

# Example for a ListCreateView
from rest_framework import generics
from .serializers import ListingSerializer

class ListingListCreateView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
