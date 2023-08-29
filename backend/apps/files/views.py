from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Files
from .serializers import FileSerializer
from core.permissions import IsSubscriber


class FilesAPIView(ReadOnlyModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsSubscriber]
