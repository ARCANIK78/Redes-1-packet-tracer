from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Tarea
from .serializers import TareaSerializer

class TareaViewSet(ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
