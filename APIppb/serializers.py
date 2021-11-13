# serializers.py
from rest_framework import serializers

from .models import Images

class ImagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Images
        fields = ('id','filename', 'imagedata','password')