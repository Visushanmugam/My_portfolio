from django.contrib import admin
from visha_app1.models import PortfolioContact



class ContactAdmin(admin.ModelAdmin):
    list = [ 'name' , 'contactmail' , 'message' ]
    
admin.site.register(PortfolioContact, ContactAdmin)


# Register your models here.
