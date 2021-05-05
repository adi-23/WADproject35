from django.shortcuts import render,HttpResponse
from .models import Restaurant,Menu
from hotels.models import Place
from authentication.models import serviceprovider
from django import forms
from django.views.generic.edit import FormView

# Create your views here.

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
        

class MenuForm(forms.ModelForm):
        
        class Meta:
                model=Menu
                fields=["fooditem_name","food_type","food_cost"]
                label={
                        'fooditem_name':"Enter food item nane",
                        'food_type':"Select item type",
                        'food_cost':"Enter food price"
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




def restaurant_form(request,user_id):
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


                User=serviceprovider.objects.get(user_id=user_id)
                restaObj=Restaurant(resta_owner=User,
                                    resta_name=form['resta_name'].value(),
                                    has_AC=form['has_AC'].value(),
                                    has_delivery=form['has_delivery'].value(),
                                    has_parking=form['has_parking'].value(),
                                    resta_address=form['resta_address'].value(),
                                    resta_place=obj,
                                    restaurant_type=form['restaurant_type'].value(),
                                    resta_contact=form['resta_contact'].value())
                restaObj.save()
                return render(request,"restaurents/menuadd.html",context={'restaurant': restaObj})


         else:
            form =RestaurantForm()
            return  render(request,'restaurants/restaurantadd.html', {"form": form})

def menuadd(request,resta_id):
    
    if request.method=='POST':
        restaurant=Restaurant.objects.get(id=resta_id)
        m_form=MenuForm(request.POST)
        menuobj=Menu(restaurant=restaurant,fooditem_name=m_form['fooditem_name'].value(),food_type=m_form['food_type']).value()
        menuobj.save()        
        return 
            
        

def aboutus(request):
    return render(request,"Visitplace/AboutUs.html")


def contact(request):
    return render(request,"Visitplace/Contact.html")


def homepage(request):
    return render(request,'authentication/Serviceuserhomepage.html')