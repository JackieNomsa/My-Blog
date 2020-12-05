from django import forms

class CreatePost(forms.Form):
    title = forms.CharField(max_length=50)
    post = forms.CharField(widget=forms.Textarea)
    author = forms.CharField(max_length=30)
    my_image = forms.ImageField(required=False)