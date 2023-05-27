from django.urls import path
from .views import PlantsListView, PlantsDetailedView

urlpatterns = [
    path('plants/', PlantsListView.as_view()),
    path('plants/<int:pk>/', PlantsDetailedView.as_view()),
]