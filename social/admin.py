from django.contrib import admin
from .models import Profile, Story, Category, Comment, Post


class CategoryAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile)
admin.site.register(Story)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "body", "created_on")
