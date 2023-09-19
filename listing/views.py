from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse_lazy

# from django.views.generic import TemplateView, CreateView, DetailView
# from .models import Listing

# class HomeView(TemplateView):
#     template_name = "listing/index.html"


def listing_home(request):
    return render(request, "listing/home.html")


def listing_logout(request):
    logout(request)
    return redirect("/")
