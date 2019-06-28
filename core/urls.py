from django.urls import path
from .views import HomeBlockView, SampleBlockView

urlpatterns = [
    path('', HomeBlockView.as_view(), name="home"),
    path('sample/', SampleBlockView.as_view(), name="sample"),
]