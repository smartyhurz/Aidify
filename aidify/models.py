from django.db import models

# Create your models here.

class post(models.Model):
    image=models.ImageField(upload_to='media/', null=True, blank=True, db_column='Pimage')
    recipename= models.CharField(max_length=100)
    description= models.CharField(max_length=20000)
    author= models.CharField(max_length=100)
    
    
class contact(models.Model):
   Name= models.CharField(max_length=100)
   Mobile= models.CharField(max_length=100)
   Email= models.EmailField(max_length=100)
   Address= models.TextField(max_length=100)
   
   
class profile(models.Model):
    image=models.ImageField(upload_to='media/', null=True, blank=True, db_column='timage')
    name= models.CharField(max_length=100)
    uname= models.CharField(max_length=200)
    email= models.EmailField(max_length=100)
    address= models.TextField(max_length=100)
    aboutme= models.TextField(max_length=100)


class time(models.Model):
    username=models.CharField(max_length=200)
    date=models.DateField(max_length=200)   
    