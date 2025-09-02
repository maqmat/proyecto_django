from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=200)
    
    description = models.TextField()
    
    image = models.ImageField(blank=True, null=True, upload_to='media')

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    