from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UploadedImage
from .serializers import UploadedImageSerializer
from .image_process import analyze_colors
from django.http import JsonResponse

from django.conf import settings
import os
import json

@api_view(['POST'])
def upload_image_api(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        # print(image)
        if(image):
            uploaded_image = UploadedImage.objects.create(image=image)
            ext = str(uploaded_image).split('.')[-1]
            if(ext == 'jpg' or ext == 'png' or ext == 'bmp'):
                path = os.path.join(settings.BASE_DIR,'mediafiles',str(uploaded_image))
                result = analyze_colors(path)
                result = json.dumps(result)
                return Response({
                "success": "true",
                "code": 200,
                "result": result,
                }, status=status.HTTP_200_OK)
            else:
                uploaded_image.delete()
                return JsonResponse({'error':'invalid image format'}, status=400)
        return JsonResponse({'error':'no image uploaded'}, status=400)
    return JsonResponse(status=400)

# @api_view(['GET'])
# def get_uploaded_images(request):
#     if request.method == 'GET':
#         images = UploadedImage.objects.all()
#         serializer = UploadedImageSerializer(images, many=True)
#         return Response(serializer.data)
#     return Response(status=400)