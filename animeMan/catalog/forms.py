from django.forms import ModelForm
from .models import AnimeCatalog

class AnimeCatalogForm(ModelForm):
    class Meta:
        model = AnimeCatalog
        exclude = ()