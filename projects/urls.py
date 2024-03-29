from django.urls import path
from . import views
from .views import ProjectDelete, ProjectListView, ProjectDetailView, ProjectCreate, ProjectUpdate

projects_patterns = ([
    path('', ProjectListView.as_view(), name='projects'),
    path('<int:pk>/<slug:slug>/', ProjectDetailView.as_view(), name='project'),
    path('create/', ProjectCreate.as_view(), name='create'),
    path('update/<int:pk>/', ProjectUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', ProjectDelete.as_view(), name='delete'),
], 'projects')