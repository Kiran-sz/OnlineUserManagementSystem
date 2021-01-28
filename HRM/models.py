from django.db import models


class Users(models.Model):
    employee_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    ranking = models.FloatField()



# Create your models here.
