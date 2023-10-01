from django.urls import path

from listings import views

urlpatterns = [
    path("", views.listing_index, name="listing_index"),
    path("<int:pk>/", views.listing_detail, name="listing_detail"),
]
