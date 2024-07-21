from django.contrib import admin

# Register your models here.
from .models import profile

class profileAdmin(admin.ModelAdmin): #The admin.ModelAdmin class provides the functionality to customize the representation of the profile model in the admin interface.
    class Meta:
        model=profile
        
admin.site.register(profile,profileAdmin)
