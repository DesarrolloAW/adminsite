from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import requests
import json
from django.contrib.auth.models import User
import datetime, random


# Create your views here.


def llenar_base(request):
    """
    rol = Roles(nombre="admin")
    rol.save()
    rol = Roles(nombre="validador")
    rol.save()
    rol = Roles(nombre="observador")
    rol.save()
    rol = Roles(nombre="visitante")
    rol.save()

    geo = json.loads(requests.get("https://cip-rrd.herokuapp.com/geografia").content)
    for key in geo:
        if key != "1":
            prov = Provincias(nombre=geo[key]['nombre'])
            prov.save()
            for cant in geo[key]['cantones']:
                for k in cant:
                    canton = Cantones(nombre=k, id_provincia=prov)
                    canton.save()
                    for i in cant[k]:
                        parroquia = Parroquias(nombre=i, id_canton=canton)
                        parroquia.save()

    est1 = Estados(nombre="Activado")
    est1.save()
    est2 = Estados(nombre="Removido")
    est2.save()
    est3 = Estados(nombre="Pendiente")
    est3.save()
    est4 = Estados(nombre="Chequiando")
    est4.save()
    est5 = Estados(nombre="Aprovado")
    est5.save()
    estac = json.loads(requests.get("https://cip-rrd.herokuapp.com/estaciones").content)
    for key in estac:
        p_name = estac[key]['parish']
        if estac[key]['parish'] == "Manglar Alto" or estac[key]['parish'] == "Olon":
            p_name = "Manglaralto"
        elif estac[key]['parish'] == "Salinas":
            p_name = "Vicente Rocafuerte"
        parro = Parroquias.objects.filter(nombre=p_name)[0]
        estacion = Estaciones(id_parroquia=parro, nombre=estac[key]['name'], latitud=estac[key]['coord']['lat'], 
                longitud=estac[key]['coord']['lng'], puntosReferencia="N/A", foto=estac[key]['img'], id_estado=est1)
        estacion.save()

    usua = json.loads(requests.get("http://cip-rrd.herokuapp.com/usuarios").content)  
    for k in usua:
        auth = User(username=usua[k]['usuario'], password=usua[k]['usuario'], first_name=usua[k]['nombre'], 
                        last_name=usua[k]['apellido'], email=usua[k]['email'])
        auth.save()
        rol = Roles.objects.filter(nombre=usua[k]['rol'])[0]
        provt = usua[k]['provincia']
        if usua[k]['provincia'] == "Galápagos" or usua[k]['provincia'] == "Gauyas": 
            provt = "Guayas"
        prov = Provincias.objects.filter(nombre=provt)[0]
        est = Estados.objects.filter(id_estado=1)[0]
        u = Usuarios(auth_user=auth, institucion=usua[k]['institucion'], telefono=usua[k]['cedula'], cedula=usua[k]['cedula'], 
                    id_provincia=prov, id_rol=rol, id_estado=est)
        u.save()
       """
    obs = json.loads(requests.get(
        "https://cip-rrd.herokuapp.com/observaciones").content)
    ep = ["invierno", "verano"]
    est = Estados.objects.filter(id_estado=3)[0]
    for k in obs:
        ob = obs[k]
        p_name = ob['estacion']['Parroquia']
    
        if ob['estacion']['Parroquia'] == "Manglar Alto" or ob['estacion']['Parroquia'] == "Santa Elena":
            p_name = "Manglaralto"
        elif ob['estacion']['Parroquia'] == "Playas":
            p_name = "General Villamil"
        elif ob['estacion']['Parroquia'] == "Salinas":
            p_name = "Vicente Rocafuerte"
        p = Parroquias.objects.filter(nombre=p_name)[0]
        esta = Estaciones.objects.filter(nombre=ob['estacion']['nombre'], id_parroquia=p)[0]
        fase = Fase_lunar.objects.filter(nombre=ob['fase_lunar'])[0]
        fecha = datetime.datetime.strptime(ob["fecha"], "%d/%m/%Y").date()
        n, a = ob["observador"].split(" ")
        a_u = User.objects.filter(first_name=n)[0]
        usu = Usuarios.objects.filter(auth_user=a_u)[0]
        obser = Observaciones(epoca=ep[random.randint(0, 1)], fecha=fecha, registeredto=datetime.datetime.now(), id_usuario=usu,
            id_fase_lunar=fase, id_estacion=esta, id_estado=est)
        #obser.save()
        for md in ob["mediciones"]:
            t_ola = Tipo_oleaje.objects.filter(id_tipo=md["olas"]["tipo"])[0]
            cr = md["corriente_de_resaca"]
            if cr == "SI":
                cr = True
            else: cr = False
            #per = Periodos.objects.filter(horario=datetime.datetime.strptime(md["hora"], "%H:%M").time())[0]
            per = Periodos.objects.all()[0]
            print(per.horario)
            #medi = Mediciones(id_observacion=obser, fechaHora=datetime.datetime.now(), ola_tipo_oleaje=t_ola, corriente_resaca=cr,
             #           latitud=obser.id_estacion.latitud, longitud=obser.id_estacion.longitud, temperatura=26.0, id_periodo=per)
    return HttpResponse()
