from django.contrib import admin
from .models import *
# Register your models here.
<<<<<<< HEAD
=======
from .models import Roles, Tipo_oleaje, Periodos, Altura_rompiente, Fase_lunar, Provincias, Cantones, Parroquias, Estados, Estaciones, Usuarios, Observaciones

>>>>>>> 640ce785c28cb5f52313764580037b77a9a53b3e
admin.site.register(Roles)
admin.site.register(Tipo_oleaje)
admin.site.register(Periodos)
admin.site.register(Altura_rompiente)
admin.site.register(Fase_lunar)
<<<<<<< HEAD
admin.site.register(Parroquias)
admin.site.register(Cantones)
admin.site.register(Provincias)
admin.site.register(Estados)
admin.site.register(Mediciones)

=======
admin.site.register(Provincias)
admin.site.register(Cantones)
admin.site.register(Parroquias)
admin.site.register(Estados)
admin.site.register(Estaciones)
admin.site.register(Usuarios)
admin.site.register(Observaciones)
>>>>>>> 640ce785c28cb5f52313764580037b77a9a53b3e
