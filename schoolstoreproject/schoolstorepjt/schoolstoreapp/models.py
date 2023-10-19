from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Departments(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name


class Courses(models.Model):
    name = models.CharField(max_length=50)
    departments = models.ForeignKey(Departments, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name


class Materials(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Faculties(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name


class Latestnews(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name


class UserProfile(models.Model):

    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=20)

    # Materials Provided can be a ManyToManyField
    materials_provided = models.ManyToManyField(Materials, blank=True)

    def __str__(self):
        return self.name
