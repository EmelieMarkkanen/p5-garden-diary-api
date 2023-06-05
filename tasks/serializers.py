from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'created_at', 'updated_at', 'title', 'content', 'due_date', 'overdue', 'image']

class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'created_at', 'updated_at', 'title', 'content', 'due_date', 'overdue', 'image']