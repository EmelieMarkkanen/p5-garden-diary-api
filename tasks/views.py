from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer, TaskDetailSerializer
from garden_diary.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class TaskListView(generics.ListCreateAPIView):
    """View for listing and creating tasks."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Task.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetailedView(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting a task."""
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Task.objects.all()
