from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from .models import Post, PostImage


class PostAdmin(admin.ModelAdmin):
    pass


class PostImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(PostImage, PostImageAdmin)