# broadcast/urls.py
from django.urls import path
from .views import BroadcastDetailView, BroadcastListView  # Replace with your views

urlpatterns = [
    path('broadcasts/<int:pk>/', BroadcastDetailView.as_view(), name='broadcast-detail'),
    path('broadcasts/', BroadcastListView.as_view(), name='broadcast-list')
    # Add more URL patterns as needed
]
