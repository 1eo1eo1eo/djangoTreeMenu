from django.shortcuts import render


def home(request):
    return render(request, "menu/home.html")


def about(request):
    return render(request, "menu/about.html")
