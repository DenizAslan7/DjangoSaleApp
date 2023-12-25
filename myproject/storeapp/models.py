from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Sale(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return f" title : {self.title} , description : {self.description} , price : {self.price} "
    
class shop(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    saler = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.IntegerField()