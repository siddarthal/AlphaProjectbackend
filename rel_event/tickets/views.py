# tickets/views.py
from rest_framework import generics
from .models import Ticket
from .serializers import TicketSerializer

class YourTicketListView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class YourTicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class UserTicketListView(generics.ListAPIView):
    serializer_class = TicketSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Ticket.objects.filter(user_id=user_id)

class EventTicketListView(generics.ListAPIView):
    serializer_class = TicketSerializer

    def get_queryset(self):
        event_id = self.kwargs['event_id']
        return Ticket.objects.filter(event_id=event_id)