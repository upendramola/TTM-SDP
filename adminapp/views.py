from django.shortcuts import render

# Create your views here.
def myfunction(request):
    return render(request, "mainpage.html")
def myAbout(request):
    return render(request, "About.html")
def myLogin(request):
    return render(request, "Login.html")
def myRegister(request):
    return render(request, "Register.html")
def myContact(request):
    return render(request, "Contact.html")

