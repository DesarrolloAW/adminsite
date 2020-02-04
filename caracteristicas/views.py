from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core.mail import EmailMessage, BadHeaderError, send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

from .models import *
import requests
import json
import datetime, random

from rest_framework.response import Response
from rest_framework_jwt.views import ObtainJSONWebToken
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework_jwt.settings import api_settings
#from .serializers import *


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
        obser.save()
        for md in ob["mediciones"]:
            t_ola = Tipo_oleaje.objects.filter(id_tipo=md["olas"]["tipo"])[0]
            cr = md["corriente_de_resaca"]
            if cr == "SI":
                cr = True
            else: cr = False
            if md["hora"] == "11:20":
                md["hora"] = "11:30"
            per = Periodos.objects.filter(horario=datetime.datetime.strptime(md["hora"], "%H:%M").time())[0]
            medi = Mediciones(id_observacion=obser, fechaHora=datetime.datetime.now(), ola_tipo_oleaje=t_ola, corriente_resaca=cr,
                       latitud=obser.id_estacion.latitud, longitud=obser.id_estacion.longitud, temperatura=26.0, id_periodo=per, perfil_playa=md["orientacion_de_playa"],
                       ancho_zon_surf=md["ancho_de_zona_de_surf"], lp_flotador=md["distancia_lp_al_flotador"], lp_rompiente=md["distancia_lp_al_rompiente"],
                       crl_espacio=md["corriente_del_litoral"]["espacio"], crl_tiempo=md["corriente_del_litoral"]["tiempo"], crl_velocidad=md["corriente_del_litoral"]["velocidad"], 
                       crl_direccion=md["corriente_del_litoral"]["direccion"], vien_direccion=md["viento"]["direccion"], vien_velocidad=md["viento"]["direccion"], ola_ortogonal=md["olas"]["ortogonal"], 
                       ola_periodo_onda=md["olas"]["periodo"], ola_altura_rompiente_promedio=md["olas"]["altura_promedio"], ola_direccion=0, estado=est)
            medi.save()
            i = 1
            for alt in md["olas"]["alturas"]:
                al_r = Altura_rompiente(num_medicion=i, valor=alt, id_medicion=medi)
                al_r.save()
                i = i + 1
    """
    return HttpResponse("hello!!!")

@csrf_exempt
def sendEmail(request):
    if request.method == 'POST':
        dic = request.POST.dict()
        
        nombres = dic['nombres']
        asunto = 'Contacto de CIPRDR'
        mail = dic['correo']
        mensaje = dic['mensaje']

        if nombres != '' and len(mail.split('@')) == 2 and mensaje != '':
            textomensaje = '<br>'
            lista = mensaje.split('\n')
            c = 0
            for i in lista:
                textomensaje += i+'</br>'
                c+=1
                if len(lista)  > c :
                    textomensaje += '<br>'
            msj = '<p><strong>Nombres: </strong>'+nombres+'</p><p><strong>Correo: </strong>'+mail+'</p><strong>Mensaje: </strong>'+textomensaje+'</p>'
            msj2 = msj+'<br/><br/><br/><p>Usted se contacto con Centro Internacional del Pacífico.</p><p><strong>NO RESPONDER A ESTE MENSAJE</strong>, nosotros nos pondremos en conacto con usted de ser necesario.</p><br/>'
            try:
                send_mail('Contactanos: '+asunto, msj,'investigacioncentro63@gmail.com', ['investigacioncentro63@gmail.com'], fail_silently=False, html_message = '<html><body>'+msj+'</body></html>')
                send_mail('Correo enviado: '+asunto, msj2, 'investigacioncentro63@gmail.com', [mail], fail_silently=False, html_message= '<html><body>'+msj2+'</body></html>')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponse('Correo enviado',status=201)
    return HttpResponse(status=404)

def getObservaciones(request):
    if request.method == 'GET':
        response = dict()
        obs = Observaciones.objects.all()
        for o in obs:
            datos = dict()
            response[o.id_observacion] = datos
            datos["estacion"] = dict()
            est = o.id_estacion
            usuario = o.id_usuario.auth_user
            datos["estacion"]["id"] = est.id_estacion
            datos["estacion"]["nombre"] = est.nombre
            datos["estacion"]["Parroquia"] = est.id_parroquia.nombre
            datos["estacion"]["img"] = est.foto
            datos["fecha"] = o.fecha
            datos["fase_lunar"] = o.id_fase_lunar.nombre
            datos["observador"] = usuario.first_name + " " + usuario.last_name
            datos["mediciones"] = list()
            meds = Mediciones.objects.filter(id_observacion=o)
            for med in meds:
                info = dict()
                info["hora"] = med.id_periodo.horario
                cl = dict()
                info["corriente_del_litoral"] = cl
                cl["espacio"] = med.crl_espacio
                cl["tiempo"] = med.crl_tiempo
                cl["direccion"] = med.crl_direccion
                cl["velocidad"] = med.crl_velocidad
                info["corriente_de_resaca"] = med.corriente_resaca
                info["ancho_de_zona_de_surf"] = med.ancho_zon_surf
                info["distancia_lp_al_flotador"] = med.lp_flotador
                info["distancia_lp_al_rompiente"] = med.lp_rompiente
                v = dict()
                info["viento"] = v
                v["velocidad"] = med.vien_velocidad
                v["direccion"] = med.vien_direccion
                info["orientacion_de_playa"] = med.perfil_playa
                ol = dict()
                info["olas"] = ol
                ol["ortogonal"] = med.ola_ortogonal
                ol["tipo"] = med.ola_tipo_oleaje.nombre
                ol["periodo"] = med.ola_periodo_onda
                ol["alturas"] = list()
                alts = Altura_rompiente.objects.filter(id_medicion=med)
                for alt in alts:
                    ol["alturas"].append(alt.valor)
                ol["altura_promedio"] = med.ola_altura_rompiente_promedio
                datos["mediciones"].append(info)
        return JsonResponse(response)

class LoginUser(ObtainJSONWebToken):

    @method_decorator(ensure_csrf_cookie)
    def post(self, request, *args, **kwargs):
        #request.data  {'username': '___', 'password': '___'}
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')

            response_data = {
                api_settings.JWT_AUTH_COOKIE: token,
                'username': user.username,
                #'es_admin_restaurante': user.es_admin_restaurante
            }
            response = Response(data=response_data)

            if api_settings.JWT_AUTH_COOKIE:
                expiration = (datetime.datetime.utcnow() +
                              api_settings.JWT_EXPIRATION_DELTA)
                response.set_cookie(api_settings.JWT_AUTH_COOKIE, token, expires=expiration, httponly=True)
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def createUser(request):
    '''
    from django.contrib.auth.models import User

    # Create user and save to the database
    user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')

    # Update fields and then save again
    user.first_name = 'John'
    user.last_name = 'Citizen'
    user.save()

    def create(self, request, *args, **kwargs):
        #  Creando un nuevo usuario
        username = request.POST.get('user.username')
        password = request.POST.get('user.password')
        # es_tecnico = request.POST.get('es_tecnico')
        es_tecnico = False
        print(username)

        user = User.objects.create_user(username, password)
        user.save()

        token = Token.objects.create(user=user)

        usuario = Usuario.objects.create(user = user, es_tecnico = es_tecnico)
        usuario.save()

    '''
    return HttpResponse(status=201)

def modifyUser(request):
    '''
    from django.contrib.auth.models import User
    u = User.objects.get(username='john')
    u.set_password('new password')
    u.save()
    '''
    return HttpResponse(status = 201)
