from django.contrib import admin

# Register your models here.
from .models import Roles, Tipo_oleaje, Periodos, Altura_rompiente, Fase_lunar, Provincias, Cantones, Parroquias, Estados, Estaciones, Usuarios, Observaciones

admin.site.register(Roles)
admin.site.register(Tipo_oleaje)
admin.site.register(Periodos)
admin.site.register(Altura_rompiente)
admin.site.register(Fase_lunar)
admin.site.register(Provincias)
admin.site.register(Cantones)
admin.site.register(Parroquias)
admin.site.register(Estados)
admin.site.register(Estaciones)
admin.site.register(Usuarios)
admin.site.register(Observaciones)
