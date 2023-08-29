from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import status
from rest_framework.response import Response
from .models import Videos
from .serializers import VideoSerializer


class YouTubeVideoAPIView(ReadOnlyModelViewSet):
   queryset = Videos.objects.all()
   serializer_class = VideoSerializer

