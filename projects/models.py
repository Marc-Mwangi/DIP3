from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Project(models.Model):
    
    
    project_name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1500)
    user = models.CharField(max_length=1500)
    
    
    def __str__(self):
        return self.project_name