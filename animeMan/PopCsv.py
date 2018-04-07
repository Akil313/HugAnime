import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'animeMan.settings')
import django 
django.setup()
from urllib.request import urlopen
from catalog.models import AnimeCatalog
from bs4 import BeautifulSoup
import csv


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


with open('../catalog_animecatalog2.csv', newline='') as animeFile:
    read = csv.reader(animeFile)
    count = 0
    # piece = (1/12294)*100
    # progress = 0'
    ids = []
    aDb = AnimeCatalog.objects.values()
    for data in aDb:
        ids.append(data['anime_id'])

    for row in read:
        if 'anime_id' in row[0] == '':
            pass
        else:
            try:
                if row[0] not in ids:
                    animeFile = AnimeCatalog.objects.get_or_create(anime_id = row[0], name = row[1].replace('&#039;', ''), genre = row[2], typeanime = row[3], episodes = row[4], rating = row[5], members = row[6], anime_url = findAnimePic(row[0]))
                    # progress+= piece
                    count += 1
                    print ('Counter: ', count, row, "\n")
                    # print (row)
                else:
                    animeFile = AnimeCatalog.objects.get_or_create(anime_id = row[0], name = row[1].replace('&#039;', ''), genre = row[2], typeanime = row[3], episodes = row[4], rating = row[5], members = row[6], anime_url = row[7])
            except:
                animeFile = AnimeCatalog.objects.get_or_create(anime_id = row[0], name = row[1].replace('&#039;', ''), genre = row[2], typeanime = row[3], episodes = row[4], rating = row[5], members = row[6], anime_url = None)
