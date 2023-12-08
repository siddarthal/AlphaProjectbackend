# events/urls.py
from django.urls import path
from .views import YourEventListView, YourEventDetailView, send_email_to_customer  # Replace with your views

urlpatterns = [
    path('events/', YourEventListView.as_view(), name='event-list'),
    path('events/<int:pk>/', YourEventDetailView.as_view(), name='event-detail'),
    path('send/', send_email_to_customer, name="send email")
    # Add more URL patterns as needed
]
