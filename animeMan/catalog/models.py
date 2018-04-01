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
    anime_id = UUIDField(primary_key = True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=100)
    Genre = CharField(max_length=300)
    type_Anime = CharField(max_length = 10)
    rating = DecimalField(max_digits = 4, decimal_places = 2)
    members = IntegerField()
    anime_cover = ImageField(blank = True, null = True, upload_to = "img/animeCover", verbose_name = "Profile Photo")