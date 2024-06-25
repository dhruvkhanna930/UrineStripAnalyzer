from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UploadedImage
from .serializers import UploadedImageSerializer
from .image_process import analyze_colors

@api_view(['POST'])
def upload_image_api(request):
    if request.method == 'POST':
        serializer = UploadedImageSerializer(data=request.data)
        if serializer.is_valid():
            uploaded_image = serializer.save()
            colors = analyze_colors(uploaded_image.image.path)
            return Response({'colors': colors}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
