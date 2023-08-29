from django.db import models
from core.models import BaseModel


class Files(BaseModel):
    tite = models.CharField(max_length=212, default="No title")
    file = models.FileField(upload_to='files')

    def __str__(self):
        return f"{self.tite}"

