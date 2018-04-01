from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .forms import AnimeCatalogForm
from .models import AnimeCatalog
# Create your views here.
def index(request):
    #allRecords = 
    return HttpResponse("Within the Catalog")

class form(View):
    def get(self, request):
        animeCatForm = AnimeCatalogForm()
        return render(request, 'catalogs/add.html', {
            'form' : animeCatForm
        })
        #return HttpResponse("Will display Anime records ")

    def post(self, request):
        animeCatForm =  AnimeCatalogForm()
        if request.method == 'POST':
            animeCatForm = AnimeCatalogForm(request.POST, request.FILES)
            if animeCatForm.is_valid():
                anime = AnimeCatalog()
                anime.name = animeCatForm.cleaned_data['name']
                anime.genre =  animeCatForm.cleaned_data['genre']
                anime.typeanime =  animeCatForm.cleaned_data['typeanime']
                anime.rating =  animeCatForm.cleaned_data['rating']
                anime.members =  animeCatForm.cleaned_data['members']
                anime.anime_cover =  animeCatForm.cleaned_data['anime_cover']
                animeCatForm.save()
                return HttpResponseRedirect("/?openr=cat&res=true")
        return render(request, 'catalogs/add.html', {
            'form' : animeCatForm
        })
        #return HttpRespons)e("Will save a new anime to the list in the database.")