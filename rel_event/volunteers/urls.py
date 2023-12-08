# volunteers/urls.py
from django.urls import path
from .views import YourVolunteerListView, YourVolunteerDetailView  # Replace with your views

urlpatterns = [
    path('volunteers/', YourVolunteerListView.as_view(), name='volunteer-list'),
    path('volunteers/user/<int:user_id>/event/<int:event_id>/', YourVolunteerDetailView.as_view(), name='volunteer-detail'),
    # Add more URL patterns as needed
]
