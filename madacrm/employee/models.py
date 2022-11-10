from django.db import models
from datetime import datetime
class employee(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.username
    
class service(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    discription=models.TextField()
    def __str__(self):
        return self.name
class coustomer(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    phonenumber=models.CharField(max_length=10,null=True,blank=True)
    city=models.CharField(max_length=100,null=True,blank=True)
    registerdate=models.DateTimeField(default=datetime.now(),null=True,blank=True)
    services=models.ManyToManyField(service,null=True,blank=True)
    def __str__(self):
        return self.name

# Create your models here.
