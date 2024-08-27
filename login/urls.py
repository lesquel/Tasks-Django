from django.urls import path
from . import views

urlpatterns = [
    path('signup',views.singUp,name='singUp'),
    path('login',views.loginPage,name='loginPage'),
    path("logout",views.logoutPage,name='logoutPage'),
]