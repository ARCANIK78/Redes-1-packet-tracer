# djangosistema_admin/views.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Define la URL para la vista dashboard
]