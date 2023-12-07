# announcements/urls.py
from django.urls import path
from .views import YourAnnouncementDetailView, YourAnnouncementListView

urlpatterns = [
    path('announcements/<int:pk>/', YourAnnouncementDetailView.as_view(), name='announcement-detail'),
    path('announcements/', YourAnnouncementListView.as_view(), name='announcement-list'),
    # Add more URL patterns as needed
]
