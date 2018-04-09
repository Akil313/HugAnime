'''
Imported necessary model fields to support the creation of a form and the fields for the database.
'''
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
'''
Anime Catalog model used for form layout as well as database fields
'''
class AnimeCatalog(models.Model):
    anime_id = CharField(primary_key = True, max_length=100) '''anime_id holds the unique identification number for each anime'''
    name = CharField(max_length=300, default = '') '''name holds the name of the anime'''
    genre = CharField(max_length=300, default = '') '''genre holds the various categories for each anime'''
    typeanime = CharField(max_length = 10, default = '') '''typeAnime holds the type of anime it is, either being TV, Movie or OVA'''
    episodes = CharField(max_length=300, default = '') ''' episodes holds the number of episode the anime has that was last recorded'''
    rating = CharField(max_length=300, default = '') '''rating holds the average rating of the anime''' 
    members = CharField(max_length=300, default = '') '''members holds the number of members that are accounted for in the ratings'''
    anime_url = CharField(max_length=300, default= None, blank = True, null = True) '''anime_url holds the url of the anime image.'''