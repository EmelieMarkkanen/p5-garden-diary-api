from rest_framework import generics, status
from .models import Plants
from .serializers import PlantsSerializer, PlantsDetailSerializer
from garden_diary.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404


class PlantsListView(generics.ListCreateAPIView):
    queryset = Plants.objects.all()
    serializer_class = PlantsSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Plants.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PlantsDetailedView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plants.objects.all()
    serializer_class = PlantsDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Plants.objects.all()
