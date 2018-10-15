from django.db import models

# Create your models here.

class Fortune(models.Model):
    txt = models.CharField(max_length=100)

    def __str__(self):
        return self.txt
