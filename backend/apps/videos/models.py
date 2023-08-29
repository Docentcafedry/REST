from django.db import models
from core.models import BaseModel


class Videos(BaseModel):
    title = models.CharField(max_length=256, default="No title")
    url = models.URLField(max_length=211)

    def __str__(self):
        return f"{self.title}, created {self.created_at}"




