from rest_framework import serializers
from todo.models import *


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','todo_text', 'add_date','completed')
