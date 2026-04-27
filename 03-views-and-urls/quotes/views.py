from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

# La vista recibe el Request y devuelve un Response


# def index(request):
#     return HttpResponse("Hello, world. You're at the quotes index.")


# def greet(request, name):
#     return HttpResponse(f"Hola, {name} 👋")

# =========================
# DATOS (diccionario)
# =========================

# Clave: día
# Valor: frase
days_of_week = {
    "monday": "¿Qué es real? ¿Cómo defines lo real?",
    "tuesday": "Hay una diferencia entre conocer el camino y recorrer el camino.",
    "wednesday": "No es la cuchara.",
    "thursday": "Deja de intentar golpearme y golpéame.",
    "friday": "El cuerpo no puede vivir sin la mente.",
    "saturday": "No conozco el futuro, vine a decirte cómo va a empezar.",
    "sunday": "Toma la pastilla roja y quédate en el País de las Maravillas."
}

# =========================
# VISTA 1: LISTAR DÍAS
# =========================

def index(request):
    list_items = ""

    # Convertimos las claves en lista
    days = list(days_of_week.keys())

    # Recorremos cada día
    for day in days:
        # Genera la URL dinámicamente usando su nombre
        day_path = reverse("day-quote", args=[day])

        # Creamos un <li> con un link
        list_items += f'<li><a href="{day_path}">{day}</a></li>'

    # Armamos HTML final
    response_html = f"<ul>{list_items}</ul>"

    return HttpResponse(response_html)


# =========================
# VISTA 2: DÍA POR NÚMERO
# =========================

def days_week_with_number(request, day):
    days = list(days_of_week.keys())

    # Validamos si el número existe
    if day > len(days):
        return HttpResponseNotFound("<h1>El día no existe ❌</h1>")

    # Convertimos número → día
    redirect_day = days[day - 1]

    # Redirige a la URL del día
    redirect_path = reverse("day-quote", args=[redirect_day])

    return HttpResponseRedirect(redirect_path)


# =========================
# VISTA 3: DÍA POR NOMBRE
# =========================

def days_week(request, day):
    try:
        # Buscar frase por día
        quote_text = days_of_week[day]

        return HttpResponse(quote_text)

    except KeyError:
        # Si no existe el día
        return HttpResponseNotFound("<h1>Este día no existe ❌</h1>")