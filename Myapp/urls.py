from django.urls import path
from Myapp.views import *
urlpatterns = [
    path('',index,name='index'),
    path('add',add,name='add'),
    path('home',index,name='index'),
    path('login',login,name='login'),
    path('patient',patient,name='login'),
    path('DoctorSignin',dsn,name="DocLogin"),
    path('DoctorSignup',dsp,name="PatientLogin"),
    path('PatientSignin',psn,name="DocLogin"),
    path('PatientSignup',psp,name="PatientLogin"),
    path('Logout',logout,name="logout"),
    path('addpost',addpost,name="addpost"),
    path('mypost',mypost,name="mypost"),

]