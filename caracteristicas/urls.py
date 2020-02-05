from django.urls import path,include
from . import views
from rest_framework import routers
"""router = routers.DefaultRouter()
router.register('mediciones', views.MedicionesViewSet)
router.register('fase', views.FaseLunarViewSet)
router.register('observacion', views.ObservacionViewSet)
router.register('provincia', views.ProvinciaViewSet)
router.register('canton', views.CantonViewSet)
router.register('parroquia', views.ParroquiaViewSet)"""

urlpatterns = [
    path('sendEmail/', views.sendEmail),
    path('ingresar/', views.llenar_base),
    path('observaciones/', views.getObservaciones),
    path('postObservaciones/', views.postObservaciones),
    #path('',include(router.urls)),
]