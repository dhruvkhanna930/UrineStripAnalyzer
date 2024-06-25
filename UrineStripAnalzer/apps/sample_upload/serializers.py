from rest_framework import serializers
from rest_framework.serializers import ValidationError
from .models import UploadedImage

class UploadedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = ['image']

    def validate(self, data):
        image = data.get('image')
        if image.size > 1024 * 1024 * 3:
            raise ValidationError("Image size should not exceed 3 MB")
        return data

    def create(self, validated_data):
        image = UploadedImage.objects.create(**validated_data)
        return image