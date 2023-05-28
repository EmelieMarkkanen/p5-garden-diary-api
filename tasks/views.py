from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer, TaskDetailSerializer
from garden_diary.permissions import IsOwnerOrReadOnly

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

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(owner=user)

    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs['pk']
        obj = generics.get_object_or_404(queryset, pk=pk)
        return obj
