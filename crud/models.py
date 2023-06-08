from django.db import models

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=50)
    roll=models.CharField(max_length=100)
    email=models.CharField(max_length=150)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)