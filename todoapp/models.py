from django.db import models



# Create your models here.
class players(models.Model):
     name = models.CharField(max_length=500)
     nationality = models.CharField(max_length=500)
     state = models.CharField(max_length=500)
     matches = models.IntegerField()
     runs = models.IntegerField()
     average = models.CharField(max_length=50)
     wickets = models.IntegerField()
     date = models.DateField()
     # img = models.ImageField(upload_to='pics')
