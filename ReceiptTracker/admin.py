from django.contrib import admin
from .models import  Receipt

#to save the data coming from Models in admin panal 
admin.site.register(Receipt)
