from django.urls import path
from .views import YouTubeVideoAPIView

app_name = "videos"

urlpatterns = [
    path("latest_videos/", YouTubeVideoAPIView.as_view())
]

