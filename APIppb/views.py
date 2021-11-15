from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import ImagesSerializer
from .models import Images
from django.template import loader


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all().order_by('filename')
    serializer_class = ImagesSerializer

def ViewImages(request):
    images = Images.objects.all().order_by('filename')
    template = loader.get_template('./images.html')
    context = {
        'images': images,
    }
    return HttpResponse(template.render(context, request))