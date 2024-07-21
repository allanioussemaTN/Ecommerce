from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class profile(models.Model):
    first_name = models.CharField(blank=False, max_length=120,default='')
    last_name = models.CharField(blank=False, max_length=120,default='')
    description = models.TextField(default='default description')
    street = models.CharField(blank=False,max_length=120,default='')
    house_number= models.CharField(blank=False,max_length=120,default='')
    Postal_code= models.CharField(blank=False,max_length=120,default='')
    city= models.CharField(blank=False,max_length=120,default='')
    country=models.CharField(blank=False,max_length=120,default='')
    email=models.EmailField(blank=False,unique=True,default='')
    phone=PhoneNumberField(blank=False,null=True,unique=True, help_text="Enter phone number with country code.")
    sum_purchase=models.CharField(max_length=120,default='')
    birthday = models.DateField(null=True, blank=True,help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    
    def __unicode__(self):
        return self.name 
