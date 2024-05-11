from django.db import models

# add doctor model
class Doctor_Details(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    age=models.IntegerField(max_length=20)
    specilist=models.CharField(max_length=30)
    date=models.DateField()
    mobile_number=models.CharField(max_length=20)
    
