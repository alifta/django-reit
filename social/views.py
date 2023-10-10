from django.shortcuts import render

from .models import Profile


def social(request):
    return render(request, "social_base.html")


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "social/profile_list.html", {"profiles": profiles})


def profile_detail(request, pk):
    # If user doesn't have profile, create one for it
    if not hasattr(request.user, "profile"):
        missing_profile = Profile(user=request.user)
        missing_profile.save()
    # Get the Profile with passed primary key
    profile = Profile.objects.get(pk=pk)
    follows = profile.follows.exclude(user=profile.user)
    followed = profile.followed_by.exclude(user=profile.user)
    context = {
        "profile": profile,
        "follows": follows,
        "followed": followed,
    }
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "social/profile_detail.html", context)
