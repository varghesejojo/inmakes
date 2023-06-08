from django.db import models

# Create your models here.
class Crud(models.Model):
    slnumber=models.IntegerField()
    itemname=models.CharField(max_length=250)
    description=models.TextField()