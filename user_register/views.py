from django.shortcuts import render
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from rest_framework.response import Response
from .forms import register_form,login_form
from django.contrib.auth import authenticate
import hashlib
import re
from .models import user_info

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

            name_check = re.match("^[a-zA-Z ]{2,}$", employee_name)
            hashed_password = hashlib.sha1(employee_password.encode()).hexdigest()
    
            email_check = re.match("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", employee_email)

            if not email_check:
                print("third")
                return render(request, 'employee_form.html', {'results': "Invalid Email Pattern"})
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
            if user_name==cleaned_data["user_name"] and password==cleaned_data["employee_password"]:
                return render(request, 'index.html',{'results': "User is Present"})
            
            elif user_name==cleaned_data["user_name"] and password!=cleaned_data["employee_password"]:
                return render(request, 'employee_auth.html',{'results': "Invalid Password"})
            
            elif user_name!=cleaned_data["user_name"] and password==cleaned_data["employee_password"]:
                return render(request, 'employee_auth.html',{'results': "Invalid UserName"})
            
            else:
                return render(request, 'employee_auth.html',{'results': "User Not Present"})
    return render(request, 'employee_form.html', {'form': form})

