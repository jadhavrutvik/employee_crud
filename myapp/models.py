from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id=models.IntegerField()
    emp_name=models.CharField(max_length=30)
    emp_email_id=models.EmailField(max_length=30)
    emp_gender=models.CharField(max_length=20)
    emp_phone=models.CharField(max_length=20)
    emp_dept=models.CharField(max_length=20)




class User(models.Model):
    username=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    confpassword=models.CharField(max_length=20)


class Dept(models.Model):
    add_dept=models.CharField(max_length=20)
    
    
