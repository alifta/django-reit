from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("pages.urls")),
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    # Overriding default Django "accounts/" with "users"
    # Removing "accounts/" url from "users/urls.py"
    path("users/", include("django.contrib.auth.urls")),
    path("listings/", include("listings.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
