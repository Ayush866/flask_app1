from django.urls import path

from user_register import views

urlpatterns = [
    path("",views.hello,name="a"),
    path("register/",views.register,name="register"),
    path("login/",views.login,name="login"),
]