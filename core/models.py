from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

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

class Booking (models.Model) :
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(Destinations, on_delete=models.CASCADE)

    phone = models.IntegerField()
    address = models.TextField()
    zipcode= models.IntegerField()

    visitday = models.DateField(blank =True , null = True ) 
    no_of_people = models.IntegerField() 
    payment = models.CharField(max_length=30)

    anything_else = models.TextField()

    def __str__(self):
        return str(self.user_name)
    
class Contact(models.Model):
    name =models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject =models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return str(self.email)
