from django.db import models
from unicodedata import name
from statistics import mode

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name
    


class product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category_id = models.ForeignKey(category,on_delete=models.CASCADE)
   
    def __str__(self):
        return self.name



class order(models.Model):
    productid = models.IntegerField()
    user_id = models.IntegerField()
    num =models.IntegerField()