from django.urls import path
from .views import *
#from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

from rest_framework_jwt.views import RefreshJSONWebToken,ObtainJSONWebToken

urlpatterns = [
    path('sendEmail/', sendEmail),
    path('login/', LoginUser.as_view()),
    path(r'auth/refresh/', obtain_jwt_token),

    path('profile/',ProfielView.as_view()),
    path('ingresar/', llenar_base),
    path('observaciones/', getObservaciones),
    path('provincias/', get_provincias),
    path('cantones/', get_cantones),
    path('parroquias/', get_parroquias),
    path('postObservaciones/', postObservaciones),
    path('crear_usuario/', postCreateUser),

    path('crear_estacion/', crear_estacion),
    path('estacion/', get_estacion),
    path('borrar_estacion/<int:idEstacion>', borrar_estacion),
    path('actualizar_estacion/<int:idEstacion>', actualizar_estacion),
    
]