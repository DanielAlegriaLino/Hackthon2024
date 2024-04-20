from django.shortcuts import render, redirect
from .models import Client
from .forms import FormularioRegistro
from .utils import zip_tostr
from django.http import HttpResponse
from django.http import JsonResponse

from .models import Product

import json
import numpy as np
import hnswlib
from collections import defaultdict
from openai import OpenAI
from dotenv import load_dotenv
import random
import string
import json
import numpy as np
import hnswlib
from collections import defaultdict
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

load_dotenv() 
client = OpenAI()

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
<<<<<<< HEAD
    return render(request, 'register_form.html', {'form': form})

@csrf_exempt
def get_best_n_products(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON in request body'}, status=400)

        # Extract search parameters
        search_query = data.get('query')
        
        productos = Product.objects.all()
        c_db = []
        c_embeddings = [] 
        for product in productos:
            c_db.append({
                "name":product.name,
                "description":product.description
                })
            c_embeddings.append(product.embedding)
        
        res = search(db=c_db,embeddings=c_embeddings,search=search_query)     
        return JsonResponse(res)
        

def search(db, embeddings, search):
    embeddings= np.array(embeddings)
    dimension = embeddings.shape[1]
    p = hnswlib.Index(space='cosine', dim=dimension)
    p.init_index(max_elements=10_000, ef_construction=200, M=16)
    p.add_items(embeddings)
    p.set_ef(50) # ef should always be > k
    new_embedding = get_embedding(search)
    # Fetch k neighbors
    labels, distances = p.knn_query(new_embedding, k=10)
    all_urls = []
    for item in db:
        all_urls.append(item)
    
    res = {}
    for i in range(5):
        res[i]= all_urls [ int(labels[0][i]) ]
        res[i].update({"distance": str(distances[0][i]) })
        
    return res

def get_embedding(text_to_embed):
	response = client.embeddings.create(
    	model="text-embedding-3-small",
    	input=[text_to_embed]
	)
	embedding = response.data[0].embedding
	return embedding
=======
    return render(request, 'registro.html', {'form': form})
>>>>>>> 1f6257d958248a72003dd84ebcae292e666f9b5c
    

