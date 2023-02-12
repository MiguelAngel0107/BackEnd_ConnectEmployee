from django.db import models

class Customer(models.Model):

    firts_name = models.CharField(max_length=81)
    last_name = models.CharField(max_length=81)

class Employee(models.Model):

    firts_name = models.CharField(max_length=81)
    last_name = models.CharField(max_length=81)
    