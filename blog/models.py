from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=40)
    data = models.DateTimeField()
    text = models.TextField()
    image = models.ImageField(upload_to='blog_images/')

