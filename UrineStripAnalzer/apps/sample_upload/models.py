from django.db import models

from django.db import models

class UploadedImage(models.Model):
    image_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.image_id} uploaded on {self.uploaded_at}"
