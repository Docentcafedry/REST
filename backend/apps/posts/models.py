from django.db import models
from core.models import BaseModel, BaseImage
from ckeditor.fields import RichTextField
# Create your models here.


class Post(BaseModel):
    title = models.CharField(max_length=200, blank=True, null=True)
    body = RichTextField()

    def __str__(self):
        return f"{self.title}, create at {self.created_at}"


class PostImage(BaseImage):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
