from django.urls import path, include

from users import views

urlpatterns = [
    # Prefix path is users/...
    # path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
    # path("signup/", views.signup, name="signup"),
]
