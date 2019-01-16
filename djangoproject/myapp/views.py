from django.shortcuts import render

# Create your views here.

def home(request): # home이라는 html 가져다줘~
    return render(request, 'home.html')