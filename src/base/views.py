from django.shortcuts import render

def home(request):
    return render(request,"pages/home.html", {})

def sign_in(request):
    return render(request, "pages/login.html", {})

def about_us(request):
    return render(request, "pages/about_us.html", {})