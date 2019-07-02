from django.urls import path
from . import views
from .views import send_tx, send_good, history_user, send_fail

urlpatterns = [
    path('', views.send_tx, name='send'),
    path('send_good', views.send_good, name='send_good'),
    path('send_fail', views.send_fail, name='send_fail'),
    path('history', views.history, name='history'),
]