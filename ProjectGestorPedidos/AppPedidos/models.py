import uuid
from django.db import models

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
    
