from django.contrib import admin
from .models import Address, Contact, ContactMessage

# Register your models here.
admin.site.register(Address)
admin.site.register(ContactMessage)
admin.site.register(Contact)
