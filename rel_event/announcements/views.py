# announcements/views.py
from rest_framework import generics
from .models import Announcement
from .serializers import AnnouncementSerializer

class YourAnnouncementDetailView(generics.RetrieveDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

class YourAnnouncementListView(generics.ListCreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer