from django.shortcuts import render, redirect
from .models import Client
from .forms import FormularioRegistro
from .utils import zip_tostr

# Create your views here.

def home(request):
    return render(request, 'inicio.html')

def clientes(request):
    return render(request, 'clientes.html')

def mensajes(request):
    return render(request, 'mensajes.html')

def metricas(request):
    return render(request, 'metricas.html')

def lading(request):
    return render(request, 'lading.html')

def formulario_registro(request):
    if request.method == 'POST':
        form = FormularioRegistro(request.POST, request.FILES)
        if form.is_valid():
            registro = form.save()
            # archivo_ruta = registro.chat_file.path
            # texto = zip_tostr(archivo_ruta)
            # registro.text_chat = texto
            # registro.save()
            post_client = Client(
                name = registro.name, 
                company = registro.company, 
                phone_number = registro.phone_number, 
                interest_areas = registro.interest_areas,
                email = registro.email)
            post_client.save()
        
    else:
        form = FormularioRegistro()
    return render(request, 'registro.html', {'form': form})
    

