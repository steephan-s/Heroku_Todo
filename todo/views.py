from todo.models import Task
from django.shortcuts import render

def detail(request):
     return render(request, 'todo/detail.html')


