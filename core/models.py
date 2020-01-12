from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Destinations (models.Model) :
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    category = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    days = models.CharField(max_length=50)
    offer = models.BooleanField(default=False)
    valid_till = models.DateField(blank =True , null = True ) 
    inclides = models.ManyToManyField("Includes",blank = True)
    url = models.CharField(max_length = 200)

    def __str__(self):
        return self.name
    
class Includes (models.Model) :
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
