from django.shortcuts import render
from django.views import View

class Imagen(View):
    def get(self, request):
        return render(request, "imagen.html",{})
    