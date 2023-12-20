from django.db import models

# Create your models here.
class user_info(models.Model):
    employee_id = models.AutoField(primary_key = True)
    employee_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    employee_email = models.CharField(max_length=30)
    password1 = models.CharField(max_length=200)