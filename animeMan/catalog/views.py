from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import View
from .forms import AnimeCatalogForm, LoginForm
from .models import AnimeCatalog
from .WebScraping import findAnimePic
from django.contrib.auth import authenticate, login, get_user_model, logout
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
        tempName.append(line['name'].replace('&#039;', '').replace('&amp;','&'))
        tempID.append(line['anime_id'])
        tempGenre.append(line['genre'])
        tempType.append(line['typeanime'])
        tempEpisodes.append(line['episodes'])
        tempRating.append(line['rating'])
        tempMembers.append(line['members'])
        pics.append(line['anime_url'])

    for x in range(0, len(tempName), 5):
        for y in range (5):
            if not(x+y >= len(tempName)):
                fiveNames.append({'name':tempName[x+y],'img':pics[x+y],'id':tempID[x+y],'genre':tempGenre[x+y],'type':tempType[x+y],'episodes':tempEpisodes[x+y],'rating':tempRating[x+y],'members':tempMembers[x+y]})
        names.append(fiveNames)
        fiveNames = []
    # items = {'names': names, 'imgs': pics}
    animelist = names
    paginator = Paginator(animelist,20)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    #html = render(request, 'home/home.html', {'names':names})
    html = render(request, 'home/home.html', {'posts':posts})
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


# class loginView(View):
#     loginForm = LoginForm

#     def get(self, request):
#         form = self.loginForm(None)
#         return render(request, 'login/register.html', {'form': form})

#     def post(self, request):
#         form = self.loginForm(request.POST)

#         if form.is_valid():

#             user = form.save(commit=False)

#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']

#             user.set_password(password)
#             user.save()

#             #login
#             user = authenticate(username=username, password=password)

#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('home/home.html')

#         return render(request, 'register/register.html', {'form': form})

def login_view(request):
    #print request.user.is_authenticated()
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        # print request.user.is_authenticated()

    return render(request, "login/login.html", {"form": form})

def register_view(request):
    return render(request, "login.html", {})

def logout_view(request):
    logout(request)
    return render(request, "login.html", {})


