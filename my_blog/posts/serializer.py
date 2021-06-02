from rest_framework import serializers
from .models import Posts

class PostSerializer(serializers.Serializer):
    class Meta:
        model = Posts
        fields = ['id','title','post','author','my_image','date_posted','date_updated']