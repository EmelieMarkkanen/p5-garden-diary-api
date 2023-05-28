from rest_framework import generics
from .models import Plants
from .serializers import PlantsSerializer, PlantsDetailSerializer
from garden_diary.permissions import IsOwnerOrReadOnly

class PlantsListView(generics.ListCreateAPIView):
    queryset = Plants.objects.all()
    serializer_class = PlantsSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PlantsDetailedView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plants.objects.all()
    serializer_class = PlantsDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Plants.objects.filter(owner=user)

    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs['pk']
        obj = generics.get_object_or_404(queryset, pk=pk)
        return obj