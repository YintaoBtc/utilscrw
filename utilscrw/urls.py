from django.contrib import admin
from django.urls import path, include
from projects.urls import projects_patterns
from profiles.urls import profiles_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
                  path('admin/', admin.site.urls),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('', include('core.urls')),
    path('blocks/', include('blocks.urls')),
    path('projects/', include(projects_patterns)),
    path('captcha/', include('captcha.urls')),

    # Paths de auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),

    path('profiles/', include(profiles_patterns)),
    path('wallet/', include('wallet.urls')),
    path('faucet/', include('faucet.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
)

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
