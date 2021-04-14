from django.shortcuts import render
from django.http import HttpResponse
from shops.models import Shop
from django.template import loader
# Create your views here.
def shop(request):
    template=loader.get_template('shops/shops.html')
    context={}
    HttpResponse(template.render(context,request))