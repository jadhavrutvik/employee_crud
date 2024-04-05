from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import random

# Create your views here.
def admin_page(request):
    return render(request,'main.html')



def home(request):
    if "logged_in" in request.session:
        return render(request,'home.html')
    else:
        return redirect("/login/")


def display(request):
    if "logged_in" in request.session:
        d=Dept.objects.values('add_dept')
    

        
        emp=Employee.objects.all()
        context={
            'emp':emp,
            'd':d
        }

        return render(request,'display.html',context)
    else:
        return redirect('/login/')



def add(request):
    if "logged_in" in request.session:
        d=Dept.objects.values('add_dept')
        context={
            'd':d
        }
        if request.method=="POST":
            emp_id=request.POST.get('id')
            emp_name=request.POST.get('name')
            emp_email_id=request.POST.get('email')
            emp_gender=request.POST.get('gender')
            emp_phone=request.POST.get('mobile')
            emp_dept=request.POST.get('dept')
            

            emp=Employee(emp_id=emp_id,emp_name=emp_name,emp_email_id=emp_email_id,emp_phone=emp_phone,emp_dept=emp_dept,emp_gender=emp_gender)
            
            emp.save()
            return redirect('/display/')
        return render(request,'add.html',context)
    else:
        return redirect("/login/")



def update(request,id):
    if "logged_in" in request.session:
        d=Dept.objects.values('add_dept')
        
        emp=Employee.objects.get(id=id)
        
        
        context={
            'i':emp,
            'd':d
        }
        print(context)
        if request.method=="POST":
            emp.emp_id=request.POST.get('id')
            emp.emp_name=request.POST.get('name')
            emp.emp_email_id=request.POST.get('email')
            emp.emp_gender=request.POST.get('gender')
            emp.emp_phone=request.POST.get('mobile')
            emp.emp_dept=request.POST.get('dept')
            emp.save()
            return redirect('/display/')
        return render(request,'display.html',context)
    else:
        return redirect("/login/")



def delete(request,id):
    # if request.method=="POST":
    if "logged_in" in request.session:
        emp=Employee.objects.get(id=id)
        emp.delete()
        return redirect('/display/')
    else:
        return redirect("/login/")

   
    


from django.contrib.auth.hashers import make_password ,check_password



def signup(request):
    # if  User.objects.filter(password=123).exists() and User.objects.filter(username='rutvik').exists() :
    #     print('find')
    # else:
    #     print('not find')
    
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confpassword=request.POST.get('confpassword')
        if password==confpassword:
            password=make_password(password)
            confpassword=make_password(confpassword)
           

            u=User(username=username,email=email,password=password,confpassword=confpassword)
            u.save()
            return redirect('/login/')
        else:
            return HttpResponse('enter same password')
    return render(request,'signup.html')





    

def login(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        pass1=request.POST.get('pass')
        print(pass1,'--------------')
        user=User.objects.get(username=uname)

        
        
        
        
        if check_password(pass1,user.password) :
            request.session['logged_in'] = True
            return redirect('/home/')
        else:
            return HttpResponse('enter valid details')
        
    return render(request,'login.html')

def dept(request):
    if "logged_in" in request.session:

    

    
        d=Dept.objects.all()
        context={
            'd':d
        }
        if request.method=="POST":
            add_dept=request.POST.get('add_dept')
            d1=Dept(add_dept=add_dept)

            d1.save()
            return redirect('/display/')
        return render(request,'add_dept.html',context)
    return redirect("/login/")

def forgot(request):
    if "logged_in" in request.session:

        if request.method=="POST":
            email=request.POST.get('email')
            if User.objects.filter(email=email).exists():
                u=User.objects.filter(email=email)
                

                otp=random.randint(1000,9999)
                
                msg=f"Your OTP is {otp}"
                sub=f"forgot password"
                send_mail(sub,msg,'jrutvik66@gmail.com',[email],fail_silently=False)
                return render(request,'change_pass.html',{'email':email,'opt':otp})
                # return redirect('/change_pass/',{'email':email,'opt':otp})

            return redirect('/change_pass/',{'email':email,'opt':otp})
        return render(request,'login.html')
    else:
        return redirect("/login/")



def change_pass(request):
    if request.method=="POST":
        email=request.POST.get('email')
        otp=request.POST.get('otp')
        otp1=request.POST.get('otp1')
        pass1=request.POST.get('pass1')
        confpass1=request.POST.get('confpass1')
        pass1=make_password(pass1)
        confpass1=make_password(pass1)


        if otp==otp1:
            u1=User.objects.get(email=email)
            u1.password=pass1
            u1.confpassword=confpass1
            u1.save()
        return redirect('/login/')
          


        

    return render(request,'change_pass.html')

def logout(request):
    
    if "logged_in" in request.session:
        request.session.clear()
        return redirect('/')
    return redirect("/login/")
