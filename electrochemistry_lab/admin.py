from django.contrib import admin
from django.forms import BaseInlineFormSet

from .models import Person, Furnace, BookingOfFurnace


# class FurnaceUserInlineFormset(BaseInlineFormSet):
#     ...


class BookingOfFurnaceInLine(admin.TabularInline):
    model = BookingOfFurnace
    extra = 3
    # formset = FurnaceUserInlineFormset


@admin.register(Person)
class RersonAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'surname', 'telephone_number', 'email'


@admin.register(Furnace)
class FurnaceAdmin(admin.ModelAdmin):
    list_display = 'furnace_name', 'location', 'max_temperature', 'min_temperature', 'is_clean', 'serviceable'
    fields = ['location', 'furnace_name', 'max_temperature', 'min_temperature', 'is_clean', 'serviceable']
    inlines = [BookingOfFurnaceInLine]


@admin.register(BookingOfFurnace)
class BookingOfFurnaceAdmin(admin.ModelAdmin):
    list_display = 'date', 'furnace', 'person'

