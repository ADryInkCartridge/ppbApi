from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import ImagesSerializer
from .models import Images


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all().order_by('filename')
    serializer_class = ImagesSerializer