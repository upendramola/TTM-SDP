from django.urls import path
from .views import *
urlpatterns = [
        path("", myfunction, name='main'),
        path("About/",myabout,name='about'),
        path("login/",myLogin,name='Login'),
        path("Register/", myregister,  name='register'),
        path("Contact/", mycontact, name='contact')
]
