from django.shortcuts import render, redirect
from .models import Client
from .forms import FormularioRegistro
from .utils import zip_tostr,get_embedding
from django.http import HttpResponse
from django.http import JsonResponse

from .models import Product

import json
import numpy as np
# import hnswlib
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

score_frases = [
    "tengo que pensarlo, quizas en otro momento",
    "he escuchado de ustedes y me gustaria obtener algo de informacion", 
    "Me interesa comprar su porducto en este momento", 
    ]
score_embbeddings = []
for frase in score_frases:
    score_embbeddings.append(get_embedding(frase))


def home(request):
    return render(request, 'inicio.html')

def clientes(request):
    return render(request, 'clientes.html')

def mensajes(request):
    return render(request, 'mensajes.html')

def metricas(request):
    return render(request, 'metricas.html')

def lading(request):
    return render(request, 'landing.html')

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
    if(len(db)>10):
        labels, distances = p.knn_query(new_embedding, k=10)
    else:
        labels, distances = p.knn_query(new_embedding, k=len(db))
        
    all_urls = []
    for item in db:
        all_urls.append(item)
    
    res = {}
    for i in range(len(db)):
        res[i]= all_urls [ int(labels[0][i]) ]
        res[i].update({"distance": str(distances[0][i]) })
        
    
    return res


@csrf_exempt
def get_user_score(request):
    data = json.loads(request.body)
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON in request body'}, status=400)

    search_query = data.get('query')
    
    productos = Product.objects.all()
    c_db = []
    c_embeddings = score_embbeddings
    for frase in score_frases:
        c_db.append({
            "frase":frase,
        })
    
    res = search(db=c_db,embeddings=c_embeddings,search=search_query)    
    best_profile = res[0]["frase"]
    return JsonResponse({"score":score_frases.index(best_profile)+1})
        
    return JsonResponse(res)
    

