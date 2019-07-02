from django.urls import path
from . import views
from .views import FaucetCreateView, faucet_completed

urlpatterns = [
    path('', FaucetCreateView.as_view(), name='faucet'),
    path('completed', views.faucet_completed, name='faucet_completed'),
]