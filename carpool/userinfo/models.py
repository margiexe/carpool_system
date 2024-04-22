from django.db import models

# Create your models here.

class user_info(models.Model):
    name = models.CharField(blank=False, null=False, max_length=50)
    roll_no = models.CharField(blank=False, null=False, max_length=50)
    email = models.EmailField(blank=False,null=False)
    days = models.DateField(blank=False)
    way = models.CharField(blank=False, max_length=50)
    area = models.CharField(blank=False, max_length=50)

    

class Receiver(models.Model):
    r_name = models.CharField(blank=False, null=False, max_length=50)
    r_email = models.EmailField(blank=False, null=False)
    