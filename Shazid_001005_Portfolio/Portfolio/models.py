from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], null=True)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    carrer_obj = models.TextField(null=True)
    technology = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True) 
    link = models.URLField(blank=True, null=True)  
    position = models.CharField(max_length=100, null=True)
    company = models.CharField(max_length=100, null=True)
    institution = models.CharField(max_length=100, null=True)
    degree = models.CharField(max_length=100, null=True)
    field_of_study = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    message = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.user.username





