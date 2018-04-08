from django.db import models
import uuid
from django.db.models import (
    UUIDField,
    CharField,
    TextField,
    IntegerField,
    DecimalField,
    ImageField
)
# Create your models here.

class AnimeCatalog(models.Model):
    anime_id = CharField(primary_key = True, max_length=100)
    name = CharField(max_length=300, default = '')
    genre = CharField(max_length=300, default = '')
    typeanime = CharField(max_length = 10, default = '')
    episodes = CharField(max_length=300, default = '')
    rating = CharField(max_length=300, default = '')
    members = CharField(max_length=300, default = '')
    anime_url = CharField(max_length=300, default= None, blank = True, null = True)