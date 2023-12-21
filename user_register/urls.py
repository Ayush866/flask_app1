from django.urls import path

from user_register import views

urlpatterns = [
    path("",views.hello,name="a"),
    path("register/",views.register,name="register"),
    path("login/",views.login,name="login"),
    path("login1/",views.login1,name="login1"),
    path("login2/",views.login2,name="login2"),
    path("user_login/",views.check_token,name="user_login"),
    path("api_token/",views.api_token,name="user_login1"),

]
