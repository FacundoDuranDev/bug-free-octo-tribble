from django.contrib import admin
from django.urls import path
from .views import Agregar, Eliminar, Visualizar
urlpatterns = [
    path("agregar/<str:nombre>/<str:imagen>/<int:precio>/", Agregar.as_view(), name="agregar"),
    path("eliminar/<str:nombre>/", Eliminar.as_view(), name="eliminar"),
    path("visualizar/", Visualizar.as_view(), name="visualizar"),
]
