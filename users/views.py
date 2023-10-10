from django.contrib.auth import login
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from users.forms import CustomUserCreationForm


def dashboard(request):
    return render(request, "users/dashboard.html")


def register(request):
    if request.method == "GET":
        return render(request, "users/register.html", {"form": CustomUserCreationForm})
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))


# Similar to register but using Django class view
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
