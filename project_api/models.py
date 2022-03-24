from ast import BinOp
from django.db import models

# Create your models here.
class User(models.Model):
    
    picture = models.ImageField()
    user_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=1500)
    email = models.EmailField(max_length=255)
    project= models.FieldFile() 