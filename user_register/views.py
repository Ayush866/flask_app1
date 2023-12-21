from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import register_form,login_form
from django.contrib.auth import authenticate
import hashlib
import re
from .models import user_info,temporary_user_info
import jwt
from datetime import datetime, timedelta
from django.contrib.auth.models import User
count = 0

@api_view(["GET"])
def hello(request):
    if request.method=="GET":
        return render(request,"index.html")
    


@api_view(["GET", "POST"])
def register(request):
    if request.method == "GET":
        return render(request, "employee_form.html")
    elif request.method == "POST":
        form = register_form(request.POST)
        print(form)
        print("first loop")
        if form.is_valid():
            print("second loop")
            cleaned_data = form.cleaned_data
            employee_name = cleaned_data['employee_name']
            user_name = cleaned_data['user_name']
            employee_email = cleaned_data['employee_email']
            employee_password = cleaned_data['employee_password']
            data_objects = user_info.objects.all()
            for obj in data_objects:
                if obj.user_name==cleaned_data["user_name"]:
                    return render(request, 'employee_form.html', {'results': "username already exists"})


            name_check = re.match("^[a-zA-Z ]{2,}$", employee_name)
            hashed_password = hashlib.sha1(employee_password.encode()).hexdigest()
    
            email_check = re.match("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", employee_email)

            if not email_check:
                print("third")
                return render(request,'employee_form.html',{'results': "Invalid Email Pattern"})
            elif not name_check:
                print("four")
                return render(request, 'employee_form.html', {'results': "Invalid Name Pattern"})
            else:
                print("five")
                info = user_info(employee_name=employee_name, user_name=user_name,
                                 employee_email=employee_email, password1=hashed_password)
                info.save()
                return render(request, 'index.html',{'results': "Data Uploaded Successfully"})

        # If the form is not valid, you can return the form errors to the template
        print(form.errors)
        print("six")
        return render(request, 'employee_form.html', {'form': form})






# @api_view(["GET","POST"])
# def login1(request):
#     if request.method == "GET":
#         print("hello")
#         return render(request, "employee_auth.html")
#     elif request.method == "POST":
#         form = login_form(request.POST)
#         data_objects = user_info.objects.all()
#         print("first")
#         if form.is_valid():
#             cleaned_data = form.cleaned_data
#             user = authenticate(request, username=cleaned_data["user_name"], password=cleaned_data["employee_password"])
#             if user is not None:
#                 print("second")
#                 login(request, user)
#                 return redirect('a')  # Redirect to your dashboard or any other page
#             else:
#                 print("third")
#             # Authentication failed, show an error message or handle it as needed
#                 return render(request, 'employee_auth.html', {'error': 'Invalid username or password'})
#     print("fourth")
#     return render(request, 'login.html')
    #         user_name=''
    #         password=''
    #         for obj in data_objects:
    #             if obj.user_name==cleaned_data["user_name"]:
    #                 user_name=obj.user_name
    #                 password = obj.password1
    #         if user_name==cleaned_data["user_name"] and password==cleaned_data["employee_password"]:
    #             return render(request, 'index.html',{'results': "User is Present"})
            
    #         elif user_name==cleaned_data["user_name"] and password!=cleaned_data["employee_password"]:
    #             return render(request, 'employee_auth.html',{'results': "Invalid Password"})
            
    #         elif user_name!=cleaned_data["user_name"] and password==cleaned_data["employee_password"]:
    #             return render(request, 'employee_auth.html',{'results': "Invalid UserName"})
            
    #         else:
    #             return render(request, 'employee_auth.html',{'results': "User Not Present"})
    # return render(request, 'employee_form.html', {'form': form})






@api_view(["GET","POST"])
def login(request):
    if request.method == "GET":
        return render(request, "employee_auth.html")
    elif request.method == "POST":
        form = login_form(request.POST)
        data_objects = user_info.objects.all()
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user_name=''
            password=''
            for obj in data_objects:
                if obj.user_name==cleaned_data["user_name"]:
                    user_name=obj.user_name
                    password = obj.password1
            hashed_password=cleaned_data["employee_password"]
            hashed_password = hashlib.sha1(hashed_password.encode()).hexdigest()
            if user_name==cleaned_data["user_name"] and password==hashed_password:
                return render(request, 'index.html',{'results': "User is Present"})
            
            elif user_name==cleaned_data["user_name"] and password!=hashed_password:
                return render(request, 'employee_auth.html',{'results': "Invalid Password"})
            
            elif user_name!=cleaned_data["user_name"] and password==hashed_password:
                return render(request, 'employee_auth.html',{'results': "Invalid UserName"})
            
            else:
                return render(request, 'employee_auth.html',{'results': "User Not Present"})
    
    return render(request, 'employee_form.html', {'form': form})










username = "ayush123"
name = "Ayush"
password = "ayush@123"
@api_view(['GET','POST'])
def login1(request):
    if request.method == "GET":
        return Response(f'Hello There',status=200)
    elif request.method=="POST":
        name1 = request.data.get("name")
        user_name1 = request.data.get("user_name")
        password1 = request.data.get("password")
        if username!=user_name1:
            return Response(f'User Not Present {name1}',status=404)
        if password!=password1:
            return Response(f'Invalid Password {password1}',status=404)

        payload = {
            "username":username,
            "password":password
        }
        token1 = jwt.encode(payload,key="Secret",algorithm="HS256")
        return Response(f'{token1}',status=200)

@api_view(['GET','POST'])
def api_token(request):
    if request.method == "GET":
        token1 = request.META['HTTP_AUTHORIZATION']
        print(token1)
        if not token1:
            return Response("Token Not Provided")
        elif token1:
            token1 = token1.split()[1]
            decoded_token = jwt.decode(token1,key="Secret",algorithm='HS256')
            name = decoded_token.get("username")
            return Response(f"Hello {name}")
    
    else:
        return Response("Invalid Request")

#Sending Token if the user is Present
@api_view(["GET","POST"])
def login2(request):
    if request.method == "GET":
        if temporary_user_info.objects.all().exists():
            return redirect('user_login')
        else:
            form = login_form()
            return render(request, "employee_auth.html",{'form':form})
    elif request.method == "POST":
        form = login_form(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            hashed_password=cleaned_data["employee_password"]
            hashed_password = hashlib.sha1(hashed_password.encode()).hexdigest()
            data_objects = user_info.objects.all()
            for obj in data_objects:
                if obj.user_name==cleaned_data["user_name"]:
                    username=obj.user_name
                    password = obj.password1
                    user_email = obj.employee_email
            #Expiration Time of a token 
            expiration_time = datetime.utcnow() + timedelta(minutes=1)
            payload = {
                "username":username,
                "password":password,
                "email":user_email,
                'exp': expiration_time
            }
            print(payload,"hghvgv")
            if username!="" and password!="":

                if username==cleaned_data["user_name"] and password==hashed_password:
                    
                    token = jwt.encode(payload,key="Secret",algorithm="HS256")
                    info = temporary_user_info(user_name=username,password=hashed_password,
                                               user_email=user_email, 
                                               user_token=token)
                    info.save()
                    
                    
                    return redirect('user_login')
            
                elif username==cleaned_data["user_name"] and password!=hashed_password:
                    return render(request, 'employee_auth.html',{'results': "Invalid Password"})
            
                elif username!=cleaned_data["user_name"] and password==hashed_password:
                    return render(request, 'employee_auth.html',{'results': "Invalid UserName"})
            
            else:
                return render(request, 'employee_auth.html',{'results': "User Not Present"})
    
    return render(request, 'employee_form.html', {'form': form})


@api_view(["GET","POST"])
def check_token(request):
    if request.method == "GET":
        if temporary_user_info.objects.all().exists():
            data_objects = temporary_user_info.objects.first()
            username = data_objects.user_name
            useremail = data_objects.user_email
            token = data_objects.user_token
            try:
                decoded_token = jwt.decode(token, key="Secret", algorithms=['HS256'])
                if username==decoded_token.get("username"):
                    return render(request, "user_dashboard.html",{"username":username,"email":useremail})

            except jwt.ExpiredSignatureError:
                first_object = temporary_user_info.objects.first()
                if first_object:
                    first_object.delete()
                return redirect('login2')
        else:
            return redirect("login2")
    
    elif request.method == "POST":
        if temporary_user_info.objects.all().exists():
            data_objects = temporary_user_info.objects.first()
            username = data_objects.user_name
            useremail = data_objects.user_email
            token = data_objects.user_token
            decoded_token = jwt.decode(token, key="Secret", algorithms=['HS256'])
        




