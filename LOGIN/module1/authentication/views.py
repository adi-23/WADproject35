from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def indexView(request):
    return render(request,'index.html')

def dashboardView(request):
    return render(request,'dashboard.html')

def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return render(request,'index.html')
    
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'registration/login.html')

def forget(request):
    return render(request,'registration/forget.html')

def registerView(request):
   
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                print("user created")
                return redirect('login')
            
        else:
            messages.info(request,"password not matching")
            return redirect('register')

    else:
        return render(request,'registration/register.html')

def logout(request):
    auth.logout(request)
    return render(request,'index.html')


#                                             NEW TRY  


# from django.contrib.auth import login, logout,authenticate
# from django.shortcuts import redirect, render
# from django.contrib import messages
# from django.views.generic import CreateView
# from .form import CustomerSignUpForm, EmployeeSignUpForm
# from django.contrib.auth.forms import AuthenticationForm
# from .models import User

# def register(request):
#     return render(request, '../templates/register.html')

# class customer_register(CreateView):
#     model = User
#     form_class = CustomerSignUpForm
#     template_name = '../templates/customer_register.html'

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('/')

# class employee_register(CreateView):
#     model = User
#     form_class = EmployeeSignUpForm
#     template_name = '../templates/employee_register.html'

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('/')


# def login_request(request):
#     if request.method=='POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None :
#                 login(request,user)
#                 return redirect('/')
#             else:
#                 messages.error(request,"Invalid username or password")
#         else:
#                 messages.error(request,"Invalid username or password")
#     return render(request, '../templates/login.html',
#     context={'form':AuthenticationForm()})

# def logout_view(request):
#     logout(request)
#     return redirect('/')




