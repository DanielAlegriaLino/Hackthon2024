from django.shortcuts import render, redirect
from .forms import FormularioRegistro
from .utils import zip_tostr

# Create your views here.

def home(request):
    return render(request, 'home.html')

def formulario_registro(request):
    if request.method == 'POST':
        form = FormularioRegistro(request.POST, request.FILES)
        if form.is_valid():
            registro = form.save()
            archivo_ruta = registro.chat_file.path
            texto = zip_tostr(archivo_ruta)
            registro.text_chat = texto
            registro.save() 
        
    else:
        form = FormularioRegistro()
    return render(request, 'register_form.html', {'form': form})
    

