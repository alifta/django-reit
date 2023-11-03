from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import CustomUser


class Profile(models.Model):
    # One-to-one relation between Django user model and the profile table
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    # Each profile follows these other profiles
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True,
    )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    # Did the new user got created by Django
    if created:
        # Create a new profile and assign it to the new user
        user_profile = Profile(user=instance)
        user_profile.save()
        # User follows herself/himself after creation
        # user_profile.follows.set([instance.profile.id])
        user_profile.follows.add(instance.profile)  # Recommended way
        user_profile.save()


# Create a Profile for each new user.
# Instead of this we use receiver decorator
# post_save.connect(create_profile, sender=CustomUser)


class Story(models.Model):
    user = models.ForeignKey(CustomUser, related_name="stories", on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Stories"

    def __str__(self):
        return f"{self.user} " f"({self.created_at:%Y-%m-%d %H:%M}): " f"{self.body[:30]}..."


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on '{self.post}'"
