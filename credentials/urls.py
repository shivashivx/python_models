from django.urls import path
from credentials import views

app_name="credentials"

urlpatterns=[
    path("register",views.register,name="signup"),
    path("logout",views.logout,name="signout"),
    path("login",views.login,name="signin"),
    path("",views.home,name="home_page")
]