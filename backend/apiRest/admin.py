from django.contrib import admin
from .models import pyme,Producto,Categorias



class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "categoria"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["categoria"]
    list_per_page = 10

admin.site.register(pyme)
admin.site.register(Categorias)
admin.site.register(Producto,ProductoAdmin)


