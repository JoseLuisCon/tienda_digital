from django.shortcuts import render
from django.http import HttpResponse
from .models import Articulos

# Create your views here.


def busqueda_productos(request):
    return render(request, "busqueda_productos.html")


def buscar(request):
    if request.GET["producto"]:
        # mensaje = "Artículo buscado: %r" % request.GET["producto"]
        producto = request.GET["producto"]
        if len(producto) > 20:
            mensaje = "Texto de búsqueda demasiado largo"
        else:
            articulos = Articulos.objects.filter(nombre__icontains=producto)

            return render(
                request,
                "resultados_busqueda.html",
                {"articulos": articulos, "query": producto},
            )

    else:
        mensaje = "No has introducido ningún artículo"
    return HttpResponse(mensaje)
