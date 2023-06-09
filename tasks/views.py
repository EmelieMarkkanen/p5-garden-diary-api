from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer, TaskDetailSerializer
from garden_diary.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class TaskListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]
<<<<<<< HEAD
=======
    queryset = Task.objects.all()
>>>>>>> dcc3008 (Rework shoppinglist app, decided to make the lists based on individual items instead for simplicity)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetailedView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
<<<<<<< HEAD
=======
    queryset = Task.objects.all()
>>>>>>> dcc3008 (Rework shoppinglist app, decided to make the lists based on individual items instead for simplicity)
