from django.contrib import admin
from .models import Package, CustomerEvents,EventBackground

# Register your models here.
admin.site.register(Package)
admin.site.register(CustomerEvents)
admin.site.register(EventBackground)
