import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'animeMan.settings')
import django 
django.setup()
from urllib.request import urlopen
from catalog.models import AnimeCatalog
from bs4 import BeautifulSoup
import csv


def findAnimePic(animeID,animeName):
    animeName = animeName.encode('ascii', 'ignore').decode('ascii')
    link = "https://myanimelist.net/anime/" + str(animeID)
    page = urlopen(link)
    soup = BeautifulSoup(page, "html.parser")

    all_img = soup.find_all("img")
    for link in all_img:
        if link.get("alt") != None:
            if animeName in link.get("alt"):
                img = link.get("src")
                return link.get("src")


with open('../anime.csv', newline='') as animeFile:
    read = csv.reader(animeFile)

    for row in read:
        if 'anime_id' in row[0]:
            pass
        else:
            animeFile = AnimeCatalog.objects.get_or_create(anime_id = row[0], name = row[1], genre = row[2], typeanime = row[3], episodes = row[4], rating = row[5], members = row[6], anime_url = findAnimePic(row[0], row[1]))
            print (row)
