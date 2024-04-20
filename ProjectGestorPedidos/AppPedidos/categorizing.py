from openai import OpenAI
from dotenv import load_dotenv
import json
import numpy as np

load_dotenv() 

client = OpenAI()

def get_embedding(text_to_embed):
	response = client.embeddings.create(
    	model="text-embedding-3-small",
    	input=[text_to_embed]
	)
	embedding = response.data[0].embedding
	return embedding


def leer_archivo(archivo):
    lineas = []  # Lista para almacenar los fragmentos de texto
    fragmento = ''  # Variable para acumular las líneas

    with open(archivo, 'r', encoding="utf-8") as f:
        for linea in f:
            if linea.strip() == '':
                if fragmento:
                    lineas.append(fragmento)
                    fragmento = ''
            else:
                fragmento += linea
    if fragmento:
        lineas.append(fragmento)
    return lineas

embeddings = []

for ley in leyes:
    embeddings.append(get_embedding(ley))

with open('embeddings.json', 'w') as f:
    json.dump(embeddings, f)

