from django.contrib import admin
from . models import Personne 

class PersonneAdmin(admin.ModelAdmin):
    list_display = ('photo','nom','numero','date_save')
    
    
admin.site.register(Personne, PersonneAdmin)
