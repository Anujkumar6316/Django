from django.db import models

# Create your models here.
class Profile(models.Model):

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    clg_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    cgpa = models.FloatField()
    clg_from = models.DateField()
    clg_till = models.DateField()
    school_name = models.CharField(max_length=200)
    percentage = models.FloatField()
    school_till = models.DateField()
    project_name = models.CharField(max_length=200)
    about_project = models.TextField(max_length=2000)
    skills = models.TextField(max_length=2000)
