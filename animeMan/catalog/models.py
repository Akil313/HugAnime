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
    '''anime_id holds the unique identification number for each anime'''
    anime_id = CharField(primary_key = True, max_length=100) 

    '''name holds the name of the anime'''
    name = CharField(max_length=300, default = '') 

    '''genre holds the various categories for each anime'''
    genre = CharField(max_length=300, default = '') 

    '''typeAnime holds the type of anime it is, either being TV, Movie or OVA'''
    typeanime = CharField(max_length = 10, default = '') 

    ''' episodes holds the number of episode the anime has that was last recorded'''
    episodes = CharField(max_length=300, default = '') 

    '''rating holds the average rating of the anime''' 
    rating = CharField(max_length=300, default = '') 

    '''members holds the number of members that are accounted for in the ratings'''
    members = CharField(max_length=300, default = '') 
    
    '''anime_url holds the url of the anime image.'''
    anime_url = CharField(max_length=300, default= None, blank = True, null = True) 