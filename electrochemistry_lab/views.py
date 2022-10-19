from django.shortcuts import render
from datetime import date
from .models import Furnace, BookingOfFurnace


def home_view(request):
    template = '../templates/base.html'
    context = {}

    furnaces = Furnace.objects.all()

    context = {'furnaces': furnaces}

    return render(request, template, context)


def furnace_book_list(request):
    template = '../templates/furnace_booking_list.html'

    furnace_name = request.GET.get('furnace', 'Forno')

    booking = BookingOfFurnace.objects.order_by('date').filter(furnace__furnace_name=furnace_name).reverse()

    book_list = []

    for book in booking:
        print(f'book: {book}')
        print(f'book.date: {book.date}')
        print(f'book.person: {book.person}')
        tmp_dict = {'date': book.date,
                    'user': book.person}

        book_list.append(tmp_dict)

    context = {'furnace_name': furnace_name,
               'date_today': date.today(),
               'booking_list': book_list}

    return render(request, template, context)
