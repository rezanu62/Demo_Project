from django.contrib import admin
from unfold.admin import ModelAdmin

# Register your models here.
from .models import StripeCustomer


@admin.register(StripeCustomer)
class StripeCustomerAdmin(ModelAdmin):
    pass 
