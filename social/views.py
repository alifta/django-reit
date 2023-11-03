from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Profile, Post, Comment, Category
from .serialalizers import PostSerializer, CommentSerializer, CategorySerializer


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


def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "social/index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "social/category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }

    return render(request, "social/detail.html", context)


@api_view(["GET"])
def list_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    content = {"posts": serializer.data}

    return Response(content)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()
