from urllib.request import urlopen
from bs4 import BeautifulSoup
       
def findAnimePic(animeID,animeName):
    animeName = animeName.encode('ascii', 'ignore').decode('ascii')
    link = "https://myanimelist.net/anime/" + str(animeID) + "/" + animeName.replace(" ","_").replace(":","_").replace(".","_").replace("!","_").replace("/","_")
    page = urlopen(link)
    soup = BeautifulSoup(page, "html.parser")

    all_img = soup.find_all("img")
    for link in all_img:
        if link.get("alt") != None:
            if animeName in link.get("alt"):
                img = link.get("src")
                return link.get("src")

