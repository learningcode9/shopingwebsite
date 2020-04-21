from django.db import models

# Create your models here.

class Sarees(models.Model):
    img=models.ImageField()
    desc=models.TextField()
    price=models.IntegerField()
   
    
class Dresses(models.Model):
    img=models.ImageField()
    desc=models.TextField()
    price=models.IntegerField()
   
   
class Lehangas(models.Model):
    img=models.ImageField()
    desc=models.TextField()
    price=models.IntegerField() 

class products(models.Model):
    img=models.ImageField()
    desc=models.TextField()
    price=models.IntegerField()
    quantity=models.IntegerField()
    subtotal=models.IntegerField()
   
    


    



