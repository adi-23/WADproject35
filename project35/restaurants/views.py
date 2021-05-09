from django.shortcuts import render,HttpResponse,redirect
from .models import Restaurant
from hotels.models import Place
from authentication.models import serviceprovider,User
from django import forms
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    DetailView,
    UpdateView,
)


# Create your views here.
class RestaurantDetailView(DetailView):
    model=Restaurant


class RestaurantUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=Restaurant
    fields=['resta_name','has_AC','has_delivery','has_parking','restaurant_type','resta_contact','resta_place','resta_address']

    def form_valid(self, form):
        if self.request.user.is_serviceprovider :
            form.instance.resta_owner= self.request.user
            return super().form_valid(form)
        else :
            return HttpResponse('Users cannot insert the restaurant')

    def test_func(self):
        restauarnt =self.get_object()
        if self.request.user == restauarnt.resta_owner:
            return True
        return False


class RestaurantForm(forms.ModelForm):
    
    class Meta:
        model=Restaurant
        fields=["resta_name",
                "has_AC",
                "has_delivery",
                "has_parking",
                "resta_contact",
                #"resta_owner",
                "restaurant_type",
                "resta_address",
                "resta_place"]
        labels={
                'resta_name':"Enter restaurant name",
                'has_AC':"AC",
                'has_delivery':"Delivery",
                'has_parking':"Parking",
                'resta_contact':"Contact number",
                #'resta_owner':"",
                'restaurant_type':"Veg,NonVeg,Both",
                'resta_address':"Address",
                'resta_place':"Place"
        }
        

# class RestaurantFormView(FormView):
#     template_name = 'restaurants/restaurantadd.html'
#     form_class = RestaurantForm
#     #success_url = '/thanks/'
#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         form.save()
#         return super().form_valid(form)




def resta_view(request,user_id):
         if request.method=="POST":
                form=RestaurantForm(request.POST)

                k=0

                for place in Place.objects.all():
                    if place.place_name==form['resta_place'].value():
                        k=1
                        obj=place
                        break
                if k==0:
                    obj = Place(place_name=form['resta_place'].value())
                    obj.save()


                user=User.objects.get(id=user_id)
                restaObj=Restaurant(resta_owner=user,
                                    resta_name=form['resta_name'].value(),
                                    has_AC=form['has_AC'].value(),
                                    has_delivery=form['has_delivery'].value(),
                                    has_parking=form['has_parking'].value(),
                                    resta_address=form['resta_address'].value(),
                                    resta_place=obj,
                                    restaurant_type=form['restaurant_type'].value(),
                                    resta_contact=form['resta_contact'].value())
                restaObj.save()
                return render(request,"hotels/redir.html",context={'restaurant': restaObj})


         else:
            if (Restaurant.objects.filter(resta_owner_id=user_id).first()) is not None:
                temp = Restaurant.objects.filter(resta_owner_id=user_id).first()
                i=temp.id
                url = '/restaurants/restaurant/{}/'.format(i)
                return redirect(url)
        
            else:
                form= RestaurantForm()
                return render(request,'restaurants/restaurant_form.html',{'form':form})


            
        
def restaurant(request):
    places=Place.objects.all()
    return render(request,'restaurants/rest1.html',{'Place':places})




def search(request):
    result=request.GET['places']
    iid=0
    for place in Place.objects.all():
        if place.place_name==result:

            iid=place.id
            break

    rest_info= Restaurant.objects.filter(resta_place_id=iid)
    p = Place.objects.filter(id=iid)
    context={'restinfo': rest_info, }
    return render(request,"restaurants/rest1.html",{
    'Place':Place.objects.all(),
    'Restaurants':rest_info,'place':p

    })


def aboutus(request):
    return render(request,"Visitplace/AboutUs.html")


def contact(request):
    return render(request,"Visitplace/Contact.html")


def homepage(request):
    return render(request,'authentication/Serviceuserhomepage.html')