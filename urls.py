from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipe_site.common.urls')),
    path('auth/', include('recipe_site.recipe_site_auth.urls')),
    path('profile/', include('recipe_site.profiles.urls')),
    path('recipes/', include('recipe_site.recipe_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
