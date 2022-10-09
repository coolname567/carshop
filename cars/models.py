from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse 
# Create your models here.
class Car (models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    price=models.DecimalField(max_digits=7, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True)
    def get_absalute_url(self):
        return reverse('car_detail',args=[self.slug])
    def __str__(self):
        return f'{self.title}'
    