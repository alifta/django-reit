from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser
from social.models import Profile
from users.forms import CustomUserCreationForm, CustomUserChangeForm


class ProfileInline(admin.StackedInline):
    model = Profile


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ["username", "email"]
    inlines = [ProfileInline]


# class CustomUserAdmin(admin.ModelAdmin):
#     model = CustomUser
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     fields = ["username"]
#     inlines = [ProfileInline]


admin.site.register(CustomUser, CustomUserAdmin)
