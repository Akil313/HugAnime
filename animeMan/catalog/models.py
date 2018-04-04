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
    anime_id = IntegerField(primary_key = True, editable=False)
    name = CharField(max_length=300)
    genre = CharField(max_length=300)
    typeanime = CharField(max_length = 10)
    episodes = IntegerField(default=0)
    rating = DecimalField(max_digits = 4, decimal_places = 2, null = True)
    members = IntegerField()
    anime_cover = ImageField(blank = True, null = True, upload_to = "img/animeCover", verbose_name = "Profile Photo")

class AnimeCatalogNew(models.Model):
    name = CharField(max_length=300)
    genre = CharField(max_length=300)
    typeanime = CharField(max_length = 10)
    episodes = IntegerField(default=0)
    rating = DecimalField(max_digits = 4, decimal_places = 2, null = True)
    members = IntegerField()
    anime_cover = ImageField(blank = True, null = True, upload_to = "img/animeCover", verbose_name = "Profile Photo")