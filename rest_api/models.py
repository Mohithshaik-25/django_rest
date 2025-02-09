from django.db import models

class Rest_prac(models.Model):
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=10)

# Create your models here.
