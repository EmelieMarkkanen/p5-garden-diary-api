from rest_framework import generics, status
from .models import Plants
from .serializers import PlantsSerializer, PlantsDetailSerializer
from garden_diary.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404


class PlantsListView(generics.ListCreateAPIView):
    """View for listing and creating a plant post"""
    queryset = Plants.objects.all()
    serializer_class = PlantsSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Plants.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PlantsDetailedView(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting a plant post."""
    queryset = Plants.objects.all()
    serializer_class = PlantsDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Plants.objects.all()
