import uuid
from django.db import models

class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(null=False, max_length=50)
    company = models.CharField(null=False, max_length=50)
    phone_number = models.CharField(null=False, max_length=10)
    interest_areas = models.CharField(null=False , max_length=50)
    email = models.EmailField(null=True)

class Form_User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(null=False, max_length=50)
    company = models.CharField(null=False, max_length=50)
    phone_number = models.CharField(null=False, max_length=10)
    email = models.EmailField(null=True)
    interest_areas = models.CharField(null=False , max_length=50)
    date_start = models.DateTimeField(null=False)
    date_end = models.DateTimeField(null=False)
    txtfile = models.FileField(upload_to='text_files/', null=False, blank=True)
    text_conversation = models.TextField(null=True, blank=True)
    txtjson = models.JSONField(null=True, blank=True)
    
    def formatted_start_time(self):
        return self.date_start.strftime("%d/%m/%y %I:%M %p")

    def formatted_end_time(self):
        return self.date_end.strftime("%d/%m/%y %I:%M %p")

    def __str__(self):
        return f"From {self.formatted_start_time()} to {self.formatted_end_time()}"

    