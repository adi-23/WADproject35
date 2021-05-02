from django.contrib import admin
from .models import User, serviceprovider, serviceuser

# Register your models here.

admin.site.register(User)
admin.site.register(serviceprovider)
admin.site.register(serviceuser)