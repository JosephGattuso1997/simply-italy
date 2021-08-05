from django.contrib import admin

from .models import Author, Category, Favorite, Post, Comment, PostView, Signup, Gallary

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostView)
admin.site.register(Signup)
admin.site.register(Gallary)
admin.site.register(Favorite)