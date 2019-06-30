from django.urls import path
from . import views
from .views import send_tx, send_good, history_user

urlpatterns = [
    path('', views.send_tx, name='send'),
    path('send_good', views.send_good, name='send_good'),
    path('history', views.history, name='history'),
]