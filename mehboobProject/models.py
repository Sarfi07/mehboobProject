from django.db import models
from django.contrib.auth.models import AbstractUser

from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class User(AbstractUser):
    pass

class StudentsAdmission(models.Model):
    student_name = models.CharField(max_length=64)
    dob = models.DateField()
    email = models.EmailField()
    age = models.IntegerField(validators=[MaxValueValidator(21), MinValueValidator(5)])
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=264)
    phone = models.IntegerField(validators=[MaxValueValidator(9999999999), MinValueValidator(0000000000)])
    previous_school = models.CharField(max_length=64)
    previous_class = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    percentage = models.FloatField(null=True,validators=[MaxValueValidator(100), MinValueValidator(40)])

    def __str__(self) -> str:
        return f"Form ID: {self.id} Student Name:{self.student_name}"
    
class ContactRequest(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    subject = models.CharField(max_length=128)
    message = models.TextField(max_length=264)

    def __str__(self) -> str:
        return f"{self.name} wants to reachout."
