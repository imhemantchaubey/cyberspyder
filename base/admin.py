from django.contrib import admin
from .models import Phone_accounts_details,Email_accounts_details
# Register your models here.
admin.site.register(Email_accounts_details)
admin.site.register(Phone_accounts_details)