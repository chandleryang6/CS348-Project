from django.contrib import admin
from myApp.models import Artist, AddConcert

#Register your models here.
#Registers the 'Artist' and 'AddConcert' models with the Django admin site, allowing them to be managed through the Django admin interface.
admin.site.register(Artist)
admin.site.register(AddConcert)