from re import DEBUG
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from app import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("recipes/", include("goods.urls", namespace="recipes")),
    path("contact/", include("contact.urls")),
    path("personalcabinet/", include("personalCabinet.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
