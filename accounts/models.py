from django.db import models
from django.contrib.auth.models import User


class Avatar(models.Model):
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user}'