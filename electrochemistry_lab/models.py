from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    telephone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=20)


class Furnace(models.Model):
    furnace_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)  # location in laboratory
    serviceable = models.BooleanField() # tec
    max_temperature = models.PositiveIntegerField()
    min_temperature = models.PositiveIntegerField()
    is_clean = models.BooleanField()
