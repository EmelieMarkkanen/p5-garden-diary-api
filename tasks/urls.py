from django.urls import path
from .views import TaskDetailedView, TaskListView

urlpatterns = [
    path('tasks/', TaskListView.as_view()),
    path('tasks/<int:pk>/', TaskDetailedView.as_view()),
]