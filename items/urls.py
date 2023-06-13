from django.urls import path
from .views import ItemListView, ItemDetailedView


urlpatterns = [
    path('items/', ItemListView.as_view()),
    path('items/<int:pk>/', ItemDetailedView.as_view())
]
