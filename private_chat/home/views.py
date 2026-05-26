from django.shortcuts import render

# Create your views here.

def load(request):
    return render(request, 'load.html')

def login(request):
    return render(request, 'login.html')

def main(request):
    return render(request, 'main.html')