# volunteers/views.py
from rest_framework import generics
from .models import Volunteer
from .serializers import VolunteerSerializer
from django.shortcuts import get_object_or_404


class YourVolunteerListView(generics.ListCreateAPIView):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer

class YourVolunteerDetailView(generics.RetrieveDestroyAPIView):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    
    def get_object(self):
        user_id = self.kwargs.get('user_id')
        event_id = self.kwargs.get('event_id')
        volunteer = get_object_or_404(Volunteer, user_id=user_id, event_id=event_id)
        return volunteer