from django.db import models

# Create your models here.

class Destination (models.Model) :
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    category = models.CharField(max_length=30)
    price = models.IntegerField()
    days = models.CharField(max_length=50)
    offer = models.BooleanField(default=False)
    inclusions = models.TextField()
    validtill = models.CharField(max_length=20) 
    
