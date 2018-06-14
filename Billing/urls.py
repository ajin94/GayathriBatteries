from django.urls import path
from . import views

urlpatterns = [
    path('', views.billing_landing, name="billing_landing"),
]
