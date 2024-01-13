from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("herblist/", include("herblist.urls")),
    path("admin/", admin.site.urls),
]