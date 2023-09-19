from django.urls import path

from .views import listing_home, listing_logout

# from .views import HomeView, ListingCreateView, ListingDetailView, listing_list

urlpatterns = [
    # ZTM
    # path("", HomeView.as_view(), name="home"),
    # path("dashboard/", listing_list, name="listing-list"),
    # path("dashboard/listing/create/", ListingCreateView.as_view(), name="listing-create"),
    # path("dashboard/listing/<int:pk>/", ListingDetailView.as_view(), name="listing-detail"),
    # Function view
    path("", listing_home, name="home"),
    path("logout/", listing_logout, name="logout"),
]
