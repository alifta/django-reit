from django.urls import path, include

from users import views
from .views import SignUpView

urlpatterns = [
    # Prefix path is users/...
    # path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
