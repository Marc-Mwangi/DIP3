from ast import BinOp
from django.db import models

# Create your models here.
class Profile(models.Model):
    
    picture = models.ImageField()
    user_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=1500)
    email = models.EmailField(max_length=255)
    
    
    def __str__(self):
        return self.user_name