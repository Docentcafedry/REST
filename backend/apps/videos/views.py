from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class YouTubeVideoAPIView(APIView):
    def get(self, request):
        return Response({"videos": []}, status=status.HTTP_200_OK)

