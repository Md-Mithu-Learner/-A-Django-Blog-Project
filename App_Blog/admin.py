from django.contrib import admin
from App_Blog.models import Blog, Comment, Likes

# Register your models here.

@admin.register(Blog)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('author','blog_title', 'slug', 'blog_content','blog_image', 'publish_date', 'update_date',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog','user', 'comment', 'comment_date',)

@admin.register(Likes)
class Likes(admin.ModelAdmin):
    list_display = ('blog','user',)
