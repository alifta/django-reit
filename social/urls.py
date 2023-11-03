from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = "social"

router = DefaultRouter()
# router.register(r"comments", views.CommentViewSet, "comment")
router.register(r"categories", views.CategoryViewSet, "category")

urlpatterns = [
    path("", views.social, name="social"),
    path("profile/", views.profile_list, name="profile_list"),
    path("profile/<int:pk>", views.profile_detail, name="profile_detail"),
    path("api/list_posts/", views.list_posts),
    path("api/", include(router.urls)),
]
