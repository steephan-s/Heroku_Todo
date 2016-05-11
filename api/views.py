from todo.models import Task
from todo.serializers import TaskSerializer
from rest_framework import generics
from django.shortcuts import render
from rest_framework import filters

class index(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class todolistview(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering = ('-id',)
