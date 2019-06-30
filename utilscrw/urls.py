from django.contrib import admin
from django.urls import path, include
from projects.urls import projects_patterns
from profiles.urls import profiles_patterns
from django.conf import settings

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('blocks/', include('blocks.urls')),
    path('projects/', include(projects_patterns)),
    path('captcha/', include('captcha.urls')),

    # Paths de auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),

    path('profiles/', include(profiles_patterns)),
    path('wallet/', include('wallet.urls')),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)