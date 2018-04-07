from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .forms import AnimeCatalogForm
from .models import AnimeCatalog
import csv
#from 
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    tempName = []
    tempID = []
    tempGenre = []
    tempType = []
    tempEpisodes= []
    tempRating = []
    tempMembers = []
    pics = []
    fiveNames = []
    names = []

    new = AnimeCatalog.objects.values()

    for line in new: 
        tempName.append(line['name'].replace('&#039;', ''))
        tempID.append(line['anime_id'])
        tempGenre.append(line['genre'])
        tempType.append(line['typeanime'])
        tempEpisodes.append(line['episodes'])
        tempRating.append(line['rating'])
        tempMembers.append(line['members'])
        pics.append(line['anime_url'])

    for x in range(0, 100, 5):
        for y in range (5):
            if not(x+y >= len(tempName)):
                fiveNames.append({'name':tempName[x+y],'img':pics[x+y],'id':tempID[x+y],'genre':tempGenre[x+y],'type':tempType[x+y],'episodes':tempEpisodes[x+y],'rating':tempRating[x+y],'members':tempMembers[x+y]})
        names.append(fiveNames)
        fiveNames = []
    # items = {'names': names, 'imgs': pics}
    html = render(request, 'home/home.html', {'names':names})
    return html

class login(View):
    def get(self, request):
        return render(request, 'login/authentication.html')

    #def post(self,request):
        

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
                anime.episodes =  animeCatForm.cleaned_data['episodes']
                anime.rating =  animeCatForm.cleaned_data['rating']
                anime.members =  animeCatForm.cleaned_data['members']
                anime.anime_url =  animeCatForm.cleaned_data['anime_url']
                animeCatForm.save()
                return HttpResponseRedirect("/?openr=cat&res=true")
        return render(request, 'catalogs/add.html', {
            'form' : animeCatForm
        })
        #return HttpRespons)e("Will save a new anime to the list in the database.")
