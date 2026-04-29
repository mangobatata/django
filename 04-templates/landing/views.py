from django.shortcuts import render
from datetime import date
from django.http import HttpResponse

# Create your views here.


def home(request):
    today = date.today()
    

    cities = [
        {'id': 'asuncion', 'name': 'Asunción'},
        {'id': 'cde', 'name': 'Ciudad del Este'},
        {'id': 'encarnacion', 'name': 'Encarnación'},
        {'id': 'luque', 'name': 'Luque'},
        {'id': 'san_lorenzo', 'name': 'San Lorenzo'}
    ]

    return render(request, 'landing/landing.html', {
        "country": "Paraguay",
        "city": "Asunción",
        "today": today,
        "cities": cities
    })

def city_detail(request, city):
    return HttpResponse(f"Ciudad: {city}")