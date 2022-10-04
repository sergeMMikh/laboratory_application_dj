from django.contrib import admin
from .models import Person, Furnace


# from .models import Phone
#
#
# @admin.register(Phone)
# class PhoneAdmin(admin.ModelAdmin):
#     list_display = 'id', 'name', 'price', 'release_date', 'lte_exists'
#     list_filter = 'name', 'price'

@admin.register(Person)
class PhoneAdmin(admin.ModelAdmin):
    ...


@admin.register(Furnace)
class PhoneAdmin(admin.ModelAdmin):
    ...
