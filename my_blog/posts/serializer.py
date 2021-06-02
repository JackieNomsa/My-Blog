from rest_framework import serializers
from posts.models import Posts

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['id','title','post','author','my_image','date_posted','date_updated']