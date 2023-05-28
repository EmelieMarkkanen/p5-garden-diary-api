from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from garden_diary.permissions import IsOwnerOrReadOnly

class TaskListView(generics.ListCreateAPIView):
    """
    List all tasks.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a task, owner can edit och delete task. 
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]
