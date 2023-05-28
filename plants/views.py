from rest_framework import generics, status
from .models import Plants
from .serializers import PlantsSerializer, PlantsDetailSerializer
from garden_diary.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


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

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = self.request.user
            return Plants.objects.filter(owner=user)
        else:
            return Plants.objects.all()