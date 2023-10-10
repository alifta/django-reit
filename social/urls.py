from django.urls import path

from .views import social, profile_list, profile_detail

app_name = "social"

urlpatterns = [
    path("", social, name="social"),
    path("profile/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile_detail, name="profile_detail"),
]
