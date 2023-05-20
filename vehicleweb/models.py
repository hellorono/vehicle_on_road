from django.db import models

from django.shortcuts import render


from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    VEHICLE_TYPES = (
        ('Two', 'Two wheelers'),
        ('Three', 'Three wheelers'),
        ('Four', 'Four wheelers'),
    )

    vehicle_number = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_TYPES)
    vehicle_model = models.CharField(max_length=100)
    vehicle_description = models.CharField(max_length=300)
    vehicle_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.vehicle_number

class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('superadmin', 'Super admin'),
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.user.username
