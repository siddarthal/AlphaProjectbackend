# payments/urls.py
from django.urls import path
from .views import YourPaymentListView, YourPaymentDetailView  # Replace with your views

urlpatterns = [
    path('payments/', YourPaymentListView.as_view(), name='payment-list'),
    path('payments/<str:pk>/', YourPaymentDetailView.as_view(), name='payment-detail'),
    # Add more URL patterns as needed
]
