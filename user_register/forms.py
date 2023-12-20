from django import forms
from .models import user_info

class register_form(forms.Form):
    employee_name = forms.CharField(max_length=30)
    user_name = forms.CharField(max_length=30)
    employee_email = forms.CharField(max_length=30)
    employee_password = forms.CharField(max_length=200)

    
class login_form(forms.Form):
    user_name = forms.CharField(max_length=30)
    employee_password = forms.CharField(max_length=200)