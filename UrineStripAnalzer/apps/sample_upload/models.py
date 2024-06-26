from django.db import models
import uuid

from django.db import models
import os


class UploadedImage(models.Model):
    image_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='images')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name
