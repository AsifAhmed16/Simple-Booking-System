from django.urls import path, include, re_path
from .views import BookingView
from django.views.generic import TemplateView

app_name = 'api'

urlpatterns = [
    path('booking/', BookingView.as_view(), name='booking'),
]

