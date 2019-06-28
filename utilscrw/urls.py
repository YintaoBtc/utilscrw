from django.contrib import admin
from django.urls import path, include
from projects.urls import projects_patterns

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('blocks/', include('blocks.urls')),
    path('projects/', include(projects_patterns)),
]
