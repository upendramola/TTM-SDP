from django.shortcuts import render

# Create your views here.
def myfunction(request):
    return render(request, "mainpage.html")
def myabout(request):
    return render(request, "about.html")
def myLogin(request):
    return render(request, "Login.html")
def myregister(request):
    return render(request, "Register.html")
def mycontact(request):
    return render(request, "Contact.html")