from turtle import mode
from unicodedata import name
from django.db import models

# Create your models here.

class signUp(models.Model):
    name = models.CharField(max_length=30, default='')
    email = models.EmailField(default='')
    address = models.CharField(max_length=100, default='')
    number = models.PositiveIntegerField(default='')
    password = models.CharField(default='', max_length=15)
    isStu = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class studentData(models.Model):
    name = models.CharField(max_length=30, default='')
    email = models.EmailField(default='')
    city = models.CharField(default='', max_length=30)
    dob = models.DateField()
    uname = models.CharField(max_length=30)
    cname = models.CharField(max_length=30)
    pyear = models.PositiveIntegerField(default='')
    spi = models.PositiveIntegerField(default='')
    pl = models.CharField(max_length=30)
    description = models.CharField(default='', max_length=30)
    
    def __str__(self):
        return self.name


class ContactForm(models.Model):
    name = models.CharField(max_length=30, default='')
    number = models.PositiveIntegerField(default='')
    email = models.EmailField(default='')
    details = models.CharField(max_length=1000, default='')
    
    def __str__(self):
        return self.name