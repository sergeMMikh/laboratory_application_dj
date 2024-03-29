from django.contrib import admin
from .models import Person, Furnace, BookingOfFurnace


class BookingOfFurnaceInLine(admin.TabularInline):
    model = BookingOfFurnace
    extra = 3


@admin.register(Person)
class RersonAdmin(admin.ModelAdmin):
    list_display = 'first_name', 'surname', 'telephone_number', 'email'
    search_fields = ('first_name', 'surname')


@admin.register(Furnace)
class FurnaceAdmin(admin.ModelAdmin):
    list_display = 'furnace_name', 'location', 'max_temperature', \
                   'min_temperature', 'is_clean', 'serviceable'
    fields = ['location',
              'furnace_name',
              'max_temperature',
              'min_temperature',
              'is_clean',
              'serviceable']
    inlines = [BookingOfFurnaceInLine]
    list_filter = ('location',)


@admin.register(BookingOfFurnace)
class BookingOfFurnaceAdmin(admin.ModelAdmin):
    list_display = 'date', 'furnace', 'person', 'comments'
    list_filter = ('furnace',)


# @admin.register(FurnaceIPConnection)
# class BookingOfFurnaceAdmin(admin.ModelAdmin):
#     list_display = 'furnace', 'ip', 'port'
