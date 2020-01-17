from django.urls import path
from . import views

urlpatterns = [
    path('sendEmail/', views.sendEmail),
    path('ingresar/', views.llenar_base),
    path('observaciones/', views.getObservaciones),
]