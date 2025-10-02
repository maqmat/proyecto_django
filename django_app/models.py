from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):

    # OPCIONES PARA EL CAMPO CATEGORY
    CATEGORY_CHOICES = [
        ('Ropa', 'Ropa'),
        ('Electrónica', 'Electrónica'),
    ]

    title = models.CharField(max_length=200)
    
    description = models.TextField()
    
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='Ropa',
    )

    image = models.ImageField(blank=True, null=True, upload_to='media')

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})