from django.db import models
from django.contrib.auth.models import User

class PostModel(models.Model):
    PostTitle = models.CharField(max_length=150)
    PostDescription = models.TextField()
    PostImage = models.ImageField(blank=True,upload_to='images/')
    DatePosted = models.DateTimeField(null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.PostTitle


