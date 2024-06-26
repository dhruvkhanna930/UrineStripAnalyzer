from django.urls import path
from apps.sample_upload.views import upload_image_api

urlpatterns = [
    path('upload_image/', upload_image_api, name='upload_image_api'),
    #  path('results/', get_uploaded_images, name='get_uploaded_images'),
]