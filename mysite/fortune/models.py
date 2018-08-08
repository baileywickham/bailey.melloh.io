from django.db import models

# Create your models here.

class fortune(models.Model):
    txt = models.CharField(max_length=100)
    
