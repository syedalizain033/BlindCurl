
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

urlpatterns = [
    path("", include("app.urls")),
]

urlpatterns += staticfiles_urlpatterns()

