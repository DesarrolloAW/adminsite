from django.db import models

# Create your models here.


class Roles(models.Model):
    id_rol = models.AutoField(primary_key=True )
    nombre = models.CharField(max_length=25, help_text="Indique el rol")

class Tipo_oleaje(models.Model):
    id_tipo =models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=25)

class Periodos(models.Model):
    id_periodos = models.AutoField(primary_key=True )
    horario =models.DateTimeField(auto_now=False, auto_now_add=False)

class Altura_rompiente(models.Model):
    id_alt_romp = models.AutoField(primary_key=True )
    num_medicion = models.IntegerField()
    valor  = models.FloatField()
    #id_medicion =models.ForeignKey('Mediciones',models.DO_NOTHING,db_column='id_medicion')

class Fase_lunar(models.Model):
    id_fase = models.AutoField(primary_key=True )
    nombre = models.CharField(max_length=25)

class Parroquias(models.Model):
    id_parroquia = models.AutoField(primary_key=True )
    nombre = models.CharField(max_length=50)
    #"foranea" id_canton =models.ForeignKey('cantones',models.DO_NOTHING,db_column='id_canton')

class Cantones(models.Model):
    id_canton = models.AutoField(primary_key=True )
    nombre = models.CharField(max_length=50)
    #"foranea" id_provincia =models.ForeignKey('provincias',models.DO_NOTHING,db_column='id_provincia')
    
class Provincias(models.Model):
    id_provincia = models.AutoField(primary_key=True )
    nombre = models.CharField(max_length=50)

class Estados(models.Model):
    id_estado = models.AutoField(primary_key=True )
    nombre = models.CharField(max_length=20)

class Mediciones(models.Model):
    id_medicion = models.AutoField(primary_key=True)
    id_observacion = models.ForeignKey('Observaciones', models.DO_NOTHING)
    fechaHora = models.DateTimeField()
    ola_tipo_oleaje = models.ForeignKey(Tipo_oleaje, models.DO_NOTHING)
    corriente_resaca = models.BooleanField()
    latitud = models.FloatField()
    longitud = models.FloatField()
    temperatura = models.FloatField()
    id_periodo = models.ForeignKey(Periodos, models.DO_NOTHING)
    perfil_playa = models.IntegerField()
    ancho_zon_surf = models.FloatField()
    lp_flotador = models.IntegerField()
    lp_rompiente = models.IntegerField()
    crl_espacio = models.FloatField()
    crl_tiempo = models.IntegerField()
    crl_velocidad = models.FloatField()
    crl_direccion = models.CharField(max_length=1)
    vien_direccion = models.IntegerField()
    vien_velocidad = models.FloatField()
    ola_ortogonal = models.IntegerField()
    ola_periodo_onda = models.IntegerField()
    ola_altura_rompiente_promedio = models.FloatField()
    ola_direccion = models.IntegerField()
    estado = models.ForeignKey(Estados, models.DO_NOTHING)

