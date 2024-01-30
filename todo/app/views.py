from django.shortcuts import render
from rest_framework import generics
from .serializers import TaskSerializer
from .models import Task
# Create your views here.


class TaskView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()





