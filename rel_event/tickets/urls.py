# tickets/urls.py
from django.urls import path
from .views import YourTicketListView, YourTicketDetailView, UserTicketListView, EventTicketListView  # Replace with your views

urlpatterns = [
    path('tickets/', YourTicketListView.as_view(), name='ticket-list'),
    path('tickets/<int:pk>/', YourTicketDetailView.as_view(), name='ticket-detail'),
    path('user/<int:user_id>/tickets/', UserTicketListView.as_view(), name='user-tickets'),
    path('event/<int:event_id>/tickets/', EventTicketListView.as_view(), name='event-tickets'),

    # Add more URL patterns as needed
]
