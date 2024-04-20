import uuid
from django.db import models

from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv() 
client = OpenAI()

class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(null=False, max_length=50)
    company = models.CharField(null=False, max_length=50)
    phone_number = models.CharField(null=False, max_length=10)
    interest_areas = models.CharField(null=False , max_length=50)
    email = models.EmailField(null=True)
    text_chat = models.TextField(null=True, blank=True)
    txtjson = models.JSONField(null=True, blank=True)

class Form_User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(null=False, max_length=50)
    company = models.CharField(null=False, max_length=50)
    phone_number = models.CharField(null=False, max_length=10)
    email = models.EmailField(null=True)
    interest_areas = models.CharField(null=False , max_length=50)

class FileFields(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    chat_file = models.FileField(upload_to='text_files/', null=False, blank=True)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    embedding =  models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name
    

def get_embedding(description):
    response = client.embeddings.create(model="text-embedding-3-small",input=[description])
    embedding = response.data[0].embedding
    return embedding

def update_embeddings():
    products = Product.objects.all()
    for product in products:
        description = product.description
        embedding = get_embedding(description)
        product.embedding = embedding
        product.save()
