from django.shortcuts import render
from django.http import HttpResponse
import csv

# Create your views here.
def index(request):
    with open('../anime.csv', 'r') as aFile:
        csvReader = csv.DictReader(aFile)
        temp = []
        fiveNames = []
        names = []

        for line in csvReader:
            temp.append(line['name'])

        for x in range(0, len(temp), 5):
            for y in range (5):
                if not(x+y >= len(temp)):
                    fiveNames.append(temp[x+y])
            names.append(fiveNames)
            fiveNames = []

        html = render(request, 'home/home.html', {'names': names})
    return html