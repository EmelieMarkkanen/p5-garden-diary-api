from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'owner', 'created_at',
        'updated_at', 'title', 'content', 'due_date', 'overdue']

class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'owner', 'created_at',
        'updated_at', 'title', 'content', 'due_date', 'overdue']