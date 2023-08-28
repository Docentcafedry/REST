from rest_framework.serializers import ModelSerializer
from .models import Post, PostImage
from versatileimagefield.serializers import VersatileImageFieldSerializer


class PostImageSerializer(ModelSerializer):
    class Meta:
        model = PostImage
        fields = '__all__'

    image = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
            ('medium_square_crop', 'crop__400x400'),
            ('small_square_crop', 'crop__50x50')
        ]
    )


class PostSerializer(ModelSerializer):
    images = PostImageSerializer(source='postimage_set', many=True)
    class Meta:
        model = Post
        fields = '__all__'
