from django.urls import path
from . import views
from .views import send_tx, send_good

urlpatterns = [
    path('', views.send_tx, name='send'),
    path('send_good', views.send_good, name='send_good'),
]