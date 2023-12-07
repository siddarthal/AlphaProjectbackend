# broadcast/views.py
from rest_framework import generics
from .models import Broadcast
from .serializers import BroadcastSerializer

class BroadcastDetailView(generics.RetrieveAPIView):
    queryset = Broadcast.objects.all()
    serializer_class = BroadcastSerializer

class BroadcastListView(generics.ListCreateAPIView):
    queryset = Broadcast.objects.all()
    serializer_class = BroadcastSerializer