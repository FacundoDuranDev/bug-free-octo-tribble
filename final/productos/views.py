from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View
from .models import Productos
# Create your views here.
class Agregar(View):
    def get(self, request, nombre, imagen, precio):
        producto_nuevo = Productos(nombre=nombre, imagen=imagen, precio=precio)
        producto_nuevo.save()
        return render(request, "productos/agregar.html", {"nombre": nombre})
    
class Eliminar(View):
    def get(self, request, nombre):
        productos = Productos.objects.all()
        for producto in productos:
            if producto.nombre == nombre:
                eliminar = Productos.objects.get(id= producto.id)
                eliminar.delete()
        return render(request, "productos/eliminar.html", {"nombre": nombre})
    
class Visualizar(View):
    def get(self, request):
        lista_imagenes = [
            "https://lh4.googleusercontent.com/nqmsl7mf3-McPBvUu1-d39HgC4VwacgP-h2ryMpjCGklnwf-_BbBNc9JH5aYtPDnhV4cuA1urpB7402Ihn5_sWjDqb2oJ-HoDIntFwFZeoZDS8Y7jnjcS09h76xKvHPVjDPhjXnb"
        ]
        return render(request, "productos/visualizar.html", {"imagenes":lista_imagenes})