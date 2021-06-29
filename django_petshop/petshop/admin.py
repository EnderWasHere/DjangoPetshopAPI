from django.contrib import admin
from .models import Customer
from .models import Pet

admin.site.register(Pet)


class Customers(admin.ModelAdmin):
    list_display = ("id", "name", "document", "created")
    list_display_links = ("id", "name", "document")
    search_fields = ("name", "document")


admin.site.register(Customer, Customers)
