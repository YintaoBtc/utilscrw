from django.urls import path
from .views import BlockListView, BlockDetailView


urlpatterns = [
    path('', BlockListView.as_view(), name='blocks'),
    path('<int:pk>/<slug:slug>/', BlockDetailView.as_view(), name='block'),
]