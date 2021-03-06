from django.shortcuts import render,redirect
from django.contrib.auth import login, logout,authenticate
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from .form import ServiceProviderSignUpForm, ServiceUserSignUpForm


class serviceuser_register(CreateView):
    model = User
    form_class = ServiceUserSignUpForm
    template_name = "authentication/serviceuser_register.html"

    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('/')


class serviceprovider_register(CreateView):
    model = User
    form_class = ServiceProviderSignUpForm
    template_name = "authentication/serviceprovider_register.html"

    def form_valid(self, form):
        user = form.save()
       # login(self.request, user)
        return redirect('/')

def login_request(request):
    if request.method=='POST':
        #if method is POST the data sent through form
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password) #user is authenticated
            if user is not None :
                login(request,user)
                if user.is_serviceprovider:
                        return redirect('../serviceproviderhome/')
                else:
                    return redirect('../userhome/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'authentication/login.html',
    context={'form':AuthenticationForm()})

# view for logout (if user clicks logout redirects to homepage)
def logout_view(request):
    logout(request)
    return redirect('/')

def home(request):
     render(request,'travel/home.html')

def serviceproviderhome(request):
    return render(request,'authentication/userHomepage.html',context={'user': request.user})

def userhome(request):
    return render(request,'authentication/Serviceuserhomepage.html',context={'username': request.user.username})
