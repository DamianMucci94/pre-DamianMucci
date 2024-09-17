from django.contrib import admin

from . import models

admin.site.register(models.ProductoCategoria)


@admin.register(models.Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'nombre', 'stock', 'unidad_de_medida', 'precio')
    list_filter = ('categoria', 'unidad_de_medida')
    search_fields = ('nombre', 'categoria__nombre')