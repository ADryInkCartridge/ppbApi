from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import ImagesSerializer
from .models import Images
from django.http import HttpResponse


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all().order_by('filename')
    serializer_class = ImagesSerializer

def viewImages(request):
    # images = Images.objects.all()
    return HttpResponse("ehe")