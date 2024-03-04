from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Employee)
class Employee(admin.ModelAdmin):
    list_display=['emp_id','emp_name','emp_email_id','emp_gender','emp_phone','emp_dept']


@admin.register(User)
class Userregister(admin.ModelAdmin):
    list_display=['username','email','password','confpassword']


@admin.register(Dept)
class Deptregister(admin.ModelAdmin):
    list_display=['add_dept']