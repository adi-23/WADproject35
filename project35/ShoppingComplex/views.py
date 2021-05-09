from django.shortcuts import render,redirect

from hotels.models import Place
from authentication.models import serviceprovider,User
from .models import ShoppingComplex
from .forms import ShoppingComplexForm
from .filters import ShoppingComplexFilter
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ( # Used class based generic views for details and updating the information
    DetailView,
    UpdateView,
)
# Create your views here.

# Searching respective shoppingcomplex details in a specified location
def search(request):
    result=request.GET['places'] # specified location
    iid=0
    for place in Place.objects.all(): # Searching the id of specified location in the database
        if place.place_name==result:

            iid=place.id
            break

    shopping_info= ShoppingComplex.objects.filter(shoppingcomplex_place_id=iid) # Filtering the shopping complex according to the place
    p = Place.objects.filter(id=iid)
    context={'shoppinginfo': shopping_info, }
    return render(request,"ShoppingComplex/shopping.html",{ # Rendering the shopping complex details in the user specified location
    'Place':Place.objects.all(),
    'shoppingMalls':shopping_info,'place':p

    })

# Filtering and getting the shopping complex names based on doctors information
def ShoppingComplexListview(request,place_id):
    # model=Hotel
    # template_name='hotels/hotel_list.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filter'] = HotelFilter(self.request.GET, queryset=self.get_queryset())
    #     return context
    
    place=Place.objects.get(id=place_id)
    shoppingcomplex_list=ShoppingComplex.objects.filter(shoppingcomplex_place=place)
    h = ShoppingComplexFilter(request.GET,queryset=shoppingcomplex_list)

    return render(request,'ShoppingComplex/shoppingcomplex_list.html',{'filter': h,'shoppingcomplex': shoppingcomplex_list})


def form_view(request,user_id):
    
    if request.method == "POST": #If method is POST the data sent through form
        form=ShoppingComplexForm(request.POST,request.FILES)
        k=0
        places=Place.objects.all()
        for place in places: # If the serviceprovider specified place is not in the database, Add it to the table 
            if form['place'].value() == place.place_name:
                k=1
                obj=place
                break
        if k == 0:
            obj=Place(place_name=form['place'].value())
            obj.save()
         # Storing and saving the shopping complex details in the database
        h_sp=User.objects.get(id=user_id)  # Searching the user information based on user id
        shopping = ShoppingComplex(shoppingcomplex_sp=h_sp,shoppingcomplex_hasFloors=form['floors'].value(),shoppingcomplex_name=form['name'].value(),shoppingcomplex_image=form['image'].value(),shoppingcomplex_place=obj,shoppingcomplex_address=form['address'].value(),shoppingcomplex_contactinfo=form['Contactinfo'].value())
        shopping.save()
        return render(request,'authentication/Serviceuserhomepage.html')
    else: # If the serviceprovider has already added shopping complex details then get the detailed information of their shopping complex otherwise render the shopping complex form 
        if (ShoppingComplex.objects.filter(shoppingcomplex_sp_id=user_id).first()) is not None:
            temp = ShoppingComplex.objects.filter(shoppingcomplex_sp_id=user_id).first() # Looking for information of their shopping complex
            i=temp.id
            url = '/shoppingcomplex/shoppingcomplex/{}/'.format(i)
            return redirect(url)

        else:
            form= ShoppingComplexForm()
            return render(request,'ShoppingComplex/shoppingcomplex_form.html',{'form':form})

class ShoppingComplexDetailView(DetailView): # With the help of DetailView, we can get detailed information of each shopping complex 
    model=ShoppingComplex


class ShoppingComplexUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # Using UpdateView, we are updating the shopping complex details
    model=ShoppingComplex
    fields=['shoppingcomplex_name','shoppingcomplex_image','shoppingcomplex_hasFloors','shoppingcomplex_address','shoppingcomplex_place','shoppingcomplex_contactinfo']

    def form_valid(self, form): # Here, if a person is serviceprovider then he/she can edit the form instance
        if self.request.user.is_serviceprovider :
            form.instance.shoppingcomplex_sp = self.request.user # Storing the user details in the form
            return super().form_valid(form)
        else :
            return HttpResponse('Users cannot insert the shopping malls') # Only serviceprovider can edit the form, users can't edit it.

    def test_func(self):
        shoppingcomplex =self.get_object()
        if self.request.user == shoppingcomplex.shoppingcomplex_sp: # Checking whether the current login user is the owner of the shopping complex
            return True
        return False


def shoppingcomplex(request):
    places=Place.objects.all()
    return render(request,'ShoppingComplex/shopping.html',{'Place':places})


# About our Website
def aboutus(request):
    return render(request,"Visitplace/AboutUs.html")

# Information about website owners
def contact(request):
    return render(request,"Visitplace/Contact.html")


def homepage(request):
    return render(request,'authentication/Serviceuserhomepage.html')