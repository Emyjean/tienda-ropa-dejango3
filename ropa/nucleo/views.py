from django.shortcuts import render
from .models import prenda

# Create your views here.
def index(request):
    return render(request, "nucleo/index.html")

def inicioSesion(request):
    return render(request, "nucleo/inicioSesion.html")

def registro(request):
    return render(request, "nucleo/registro.html")

def recuperar(request):
    return render(request, "nucleo/recuperar.html")

def carro(request):
    prendas = prenda.objects.all()
    return render(request, "nucleo/carro.html",{'prendas': prendas})
    

