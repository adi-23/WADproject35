from django.contrib import admin
from .models import User,Serviceusers,Serviceproviders
# Register your models here.
admin.site.register('User')
admin.site.register('Serviceusers')

admin.site.register('Serviceproviders')