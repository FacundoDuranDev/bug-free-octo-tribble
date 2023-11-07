from django.shortcuts import render
from django.views import View
from .models import Gestor
# Create your views here.
class Agregar(View):
    def get(self, request, nombre):
        producto_nuevo = Gestor(nombre=nombre)
        producto_nuevo.save()
        return render(request, "gestor/agregar.html", {"nombre": nombre})
    
class Eliminar(View):
    def get(self, request, nombre):
        productos = Gestor.objects.all()
        for producto in productos:
            if producto.nombre == nombre:
                eliminar = Gestor.objects.get(id= producto.id)
                eliminar.delete()
        return render(request, "gestor/eliminar.html", {"nombre": nombre})
    
class Visualizar(View):
    def get(self, request):
        productos = Gestor.objects.all()
        return render(request, "gestor/visualizar.html", {"productos":productos})