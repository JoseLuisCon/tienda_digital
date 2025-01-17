from django.contrib import admin

# Register your models here


from .models import Clientes
from .models import Articulos
from .models import Pedidos


class ClientesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "email", "tfno")
    search_fields = ("nombre", "tfno")


class ArticulosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "seccion", "precio")
    search_fields = ("nombre", "seccion")
    list_filter = ("seccion",)


class PedidosAdmin(admin.ModelAdmin):
    list_display = ("numero", "fecha", "entregado")
    list_filter = ("fecha", "entregado")
    date_hierarchy = "fecha"


admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)
