from django.db import models
import datetime
from django.db.models.deletion import CASCADE

from django.db.models.fields.related import ForeignKey

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=50)
    post = models.TextField(null=False)
    author = models.CharField(max_length=30, default='Jackie')
    my_image = models.ImageField(null=True,blank=True, upload_to='images/')
    date_posted = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=False, auto_now=True) 

    def __str__(self):
        return self.title

class Comments(models.Model):
    comment = models.CharField(max_length=200)
    for_post = ForeignKey(Posts,on_delete=models.CASCADE)
    written_by = models.CharField(max_length=30)
    date_posted = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.comment