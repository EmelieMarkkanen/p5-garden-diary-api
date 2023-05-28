from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer, TaskDetailSerializer
from garden_diary.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class TaskListView(generics.ListCreateAPIView):
    """
    List all tasks.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a task, owner can edit och delete task. 
    """
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = self.request.user
            return Task.objects.filter(owner=user)
        else:
            return Task.objects.all()
