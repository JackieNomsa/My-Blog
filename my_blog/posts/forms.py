from django import forms
from .models import Posts, Comments

class CreatePost(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title','post','author','my_image']

class CreateComment(forms.Form):
    comment = forms.CharField(max_length=200)
    