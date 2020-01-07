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
