from uuid import uuid4
from django.db import models

# Create your models here.
class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    address =models.CharField('Address', max_length=1000)
    zip_code =models.CharField('ZIP/ Postal Code', max_length=12)
    city = models.CharField('City', max_length=1000)
    state= models.CharField('State',max_length=100)
    country = models.CharField('Country', max_length=1000)
    email = models.EmailField(max_length=70, null=True, blank=True, unique=True)
    phone = models.CharField(max_length=12)
    notes = models.TextField('Notes', blank=True)
    url = models.URLField('URL', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified =models.DateTimeField(auto_now=True)
