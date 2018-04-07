from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import View
from .forms import AnimeCatalogForm, LoginForm
from .models import AnimeCatalog
from .WebScraping import findAnimePic
from django.contrib.auth import authenticate, login
import csv

# Create your views here.
def home(request):
    with open('../anime.csv', 'r') as aFile:
        csvReader = csv.DictReader(aFile)
        temp = []
        tempID = []
        pics = []
        fiveNames = []
        names = []

        for line in csvReader:
            temp.append(line['name'].replace('&#039;', ''))
            tempID.append(line['anime_id'])

        for x in range(0,5):
            pics.append(findAnimePic(tempID[x],temp[x]))

        for x in range(0, len(temp), 5):
            for y in range (5):
                if not(x+y >= len(temp)):
                    fiveNames.append({'name':temp[x+y],'img':pics[y]})
            names.append(fiveNames)
            fiveNames = []
        #items = {'names': names, 'imgs': pics}
        html = render(request, 'home/home.html', {'names':names})
    return html

def login(request):
    return render(request, 'login/authentication.html')

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
                anime.anime_cover =  animeCatForm.cleaned_data['anime_cover']
                animeCatForm.save()
                return HttpResponseRedirect("/?openr=cat&res=true")
        return render(request, 'catalogs/add.html', {
            'form' : animeCatForm
        })
        #return HttpRespons)e("Will save a new anime to the list in the database.")


class login(View):
    loginForm = LoginForm

    def get(self, request):
        form = self.loginForm(None)
        return render(request, 'home/home.html', {'form': form})

    def post(self, request):
        form = self.loginForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            #login
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home/home.html')

        return render(request, 'home/home.html', {'form': form})


