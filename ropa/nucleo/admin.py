from django.contrib import admin
from .models import marca
from .models import talla
from .models import departamento
from .models import proveedor
from .models import cliente
from .models import prenda
from .models import venta

# Register your models here.
admin.site.register(marca)
admin.site.register(talla)
admin.site.register(departamento)
admin.site.register(proveedor)
admin.site.register(cliente)
admin.site.register(prenda)
admin.site.register(venta)

class marcaAdmin(admin.ModelAdmin):
    readonly_fields = ("create", "update")
class tallaAdmin(admin.ModelAdmin):
    readonly_fields = ("create", "update")
class departamentoAdmin(admin.ModelAdmin):
    readonly_fields = ("create", "update")
class proveedorAdmin(admin.ModelAdmin):
    readonly_fields = ("create", "update")
class clienteAdmin(admin.ModelAdmin):
    readonly_fields = ("create", "update")
class prendaAdmin(admin.ModelAdmin):
    readonly_fields = ("create", "update")
class ventaAdmin(admin.ModelAdmin):
    readonly_fields = ("create", "update")