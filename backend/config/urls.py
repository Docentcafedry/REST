"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter
from posts.views import PostViewSet
from videos.views import YouTubeVideoAPIView
from django.conf import settings
from django.conf.urls.static import static
from files.views import FilesAPIView
from home.views import HomeView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename="shops")
router.register(r'videos', YouTubeVideoAPIView, basename="videos")
router.register(r'files', FilesAPIView, basename="files")


schema_view = get_swagger_view(title="Two DEMO API")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view),
    path('home', HomeView.as_view(), name='home')
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
