import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'animeMan.settings')
import django 
django.setup()
from urllib.request import urlopen
from catalog.models import AnimeCatalog
from bs4 import BeautifulSoup
import csv

# Scrapes the website myanimelist.net using the anime's id to find the corresponding url for its picture
def findAnimePic(animeID):
    link = "https://myanimelist.net/anime/" + str(animeID)
    
    try:
        page = urlopen(link)
        soup = BeautifulSoup(page, "html.parser")

        all_img = soup.find_all("img")
        for link in all_img:
            if link.get("class") != None:
                if "ac" in link.get("class"):
                    img = link.get("src")
                    return link.get("src")
    except:
        return None


with open('../catalog_animecatalog.csv', newline='') as animeFile:
    read = csv.reader(animeFile)
    count = 0
    # piece = (1/12294)*100
    # progress = 0'
    ids = []
    aDb = AnimeCatalog.objects.values()

    #Adds ids of anime existing in mysql in a list
    for data in aDb:
        ids.append(data['anime_id'])

    #For each entry of the csv file
    for row in read:
        if 'anime_id' in row[0] == '':
            pass
        else:
            try:
                #If the anime from the csv file does not exist in the exsisting databse add the anime
                if row[0] not in ids:
                    animeFile = AnimeCatalog.objects.get_or_create(anime_id = row[0], name = row[1].replace('&#039;', ''), genre = row[2], typeanime = row[3], episodes = row[4], rating = row[5], members = row[6], anime_url = findAnimePic(row[0]))
                    print (row)
            #If an error is encountered getting the anime picture url then give it NULL in the url field
            except:
                animeFile = AnimeCatalog.objects.get_or_create(anime_id = row[0], name = row[1].replace('&#039;', ''), genre = row[2], typeanime = row[3], episodes = row[4], rating = row[5], members = row[6], anime_url = None)

    print ("Completed")
