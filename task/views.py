from django.shortcuts import render
from .models import Tasks
from rest_framework import viewsets, permissions
from .serializers import TasksSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset=Tasks.objects.all()
    serializer_class=TasksSerializer
    permission_classes=[permissions.AllowAny]