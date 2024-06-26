from django.contrib import admin
from .models import UploadedImage
# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    list_display = ["image_id", "image", "uploaded_at"]
    search_fields = ["uploaded_at"]

admin.site.register(UploadedImage, ImageAdmin)