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
        

