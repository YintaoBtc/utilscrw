from django.urls import path
from . import views
from .views import FaucetCreateView

urlpatterns = [
    path('', FaucetCreateView.as_view(), name='faucet'),
]