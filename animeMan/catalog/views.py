from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import View
from .forms import AnimeCatalogForm, LoginForm ''' Imports the anime catalog form and login for to be used for the html pages'''
from .models import AnimeCatalog ''' Imports the animeCatalog model for posting data to database'''
from django.contrib.auth import authenticate, login, get_user_model, logout 
import csv ''' Imports CSV to get data from CSV file'''
from django.core.paginator import Paginator ''' import statement for the paginator module so the anime could be displayed using pages and not be cluttered'''

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

    new = AnimeCatalog.objects.values()''' Pulls all the data from the MySQL database table, catalog_animecatalog, and stores it in the variable new'''

    ''' for each entry from the database, each record's data is stored into their own individual array'''
    for line in new: 
        tempName.append(line['name'].replace('&#039;', '').replace('&amp;','&'))
        tempID.append(line['anime_id'])
        tempGenre.append(line['genre'])
        tempType.append(line['typeanime'])
        tempEpisodes.append(line['episodes'])
        tempRating.append(line['rating'])
        tempMembers.append(line['members'])
        pics.append(line['anime_url'])

    for x in range(0, len(tempName), 5): ''' for loop to control the grouping of the entire anime collection into 5's '''
        for y in range (5): ''' control statement for every five animes'''
            if not(x+y >= len(tempName)): '''if the anime referenced is a valid anime then append it to the list of five animes'''
                fiveNames.append({'name':tempName[x+y],'img':pics[x+y],'id':tempID[x+y],'genre':tempGenre[x+y],'type':tempType[x+y],'episodes':tempEpisodes[x+y],'rating':tempRating[x+y],'members':tempMembers[x+y]})
        names.append(fiveNames) '''Append the list of five animes to the list containing the lists of 5 animes'''
        fiveNames = []
    animelist = names
    paginator = Paginator(animelist,20) ''' holds 20 entries from the list of 5 anime'''
    page = request.GET.get('page') ''' gets the respective page to render the data to'''
    posts = paginator.get_page(page) ''' gets all of the pages to be posted to the webpage'''

    ''' renders the data that has been compiled into post onto the home html file'''
    html = render(request, 'home/home.html', {'posts':posts}) 
    return html 

'''
Class for servicing the http requests of the Form
'''
class form(View): 
    ''' Gets the form and displays it to the webpage'''
    def get(self, request):
        animeCatForm = AnimeCatalogForm()
        return render(request, 'catalogs/add.html', {
            'form' : animeCatForm
        })
        #return HttpResponse("Will display Anime records ")

    ''' Takes the information entered into the form and saves it to the database'''
    def post(self, request):
        animeCatForm =  AnimeCatalogForm() ''' sets this variable to be the form'''
        if request.method == 'POST': ''' If the request made is a POST request'''
            animeCatForm = AnimeCatalogForm(request.POST, request.FILES)
            if animeCatForm.is_valid(): '''if the form is valid, clean of all the data that was received from the form and save it to the database'''
                anime = AnimeCatalog()
                anime.name = animeCatForm.cleaned_data['name']
                anime.genre =  animeCatForm.cleaned_data['genre']
                anime.typeanime =  animeCatForm.cleaned_data['typeanime']
                anime.episodes =  animeCatForm.cleaned_data['episodes']
                anime.rating =  animeCatForm.cleaned_data['rating']
                anime.members =  animeCatForm.cleaned_data['members']
                anime.anime_url =  animeCatForm.cleaned_data['anime_url']
                animeCatForm.save()
                return HttpResponseRedirect("/?openr=cat&res=true")''' Redirect page to this extension if POST was successful'''
        return render(request, 'catalogs/add.html', {
            'form' : animeCatForm
        })''' returns the form if request method is not POST'''

def login_view(request): ''' renders the login.html webpage'''
    #print request.user.is_authenticated()
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        # print request.user.is_authenticated()

    return render(request, "login/login.html", {"form": form})

''' renders the login.html webpage when logging in'''
def register_view(request):
    return render(request, "login.html", {})

''' renders the login.html webpage when logging out'''
def logout_view(request):
    logout(request)
    return render(request, "login.html", {})