from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .forms import AnimeCatalogForm
from .models import AnimeCatalog
from .WebScraping import findAnimePic
import csv

# Create your views here.
def index(request):
    with open('../anime.csv', 'r') as aFile:
        csvReader = csv.DictReader(aFile)
        temp = []
        tempID = []
        pics = []
        fiveNames = []
        names = []

        for line in csvReader:
            temp.append(line['name'])
            tempID.append(line['anime_id'])
        '''
        for x in range(len(temp)):
            pics.append(findAnimePic(tempID[x],temp[x]))
        '''
        for x in range(0, len(temp), 5):
            for y in range (5):
                if not(x+y >= len(temp)):
                    fiveNames.append(temp[x+y])
            names.append(fiveNames)
            fiveNames = []

        html = render(request, 'home/home.html', {'names': names})
    return html

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
