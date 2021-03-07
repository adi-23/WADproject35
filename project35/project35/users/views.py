from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

 
# Create your views here.
def home(request):
    return HttpResponse("homepage")


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        if User.objects.filter(username=username,password=password).exists():
            redirect('home/')
        else:
            return HttpResponse("INVALIED RESPONSE")
    else:
     return render(request,'users/login.html')   
        
        
    


