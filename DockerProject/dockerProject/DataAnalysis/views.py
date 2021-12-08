from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum, Count
import matplotlib.pyplot as plt
import RestAPI
import json
import numpy as np

@csrf_exempt
def compareSales(request):
    name1 = request.POST.get('name1')
    name2 = request.POST.get('name2')

    game1 = RestAPI.models.Game.objects.filter(name=name1)
    game2 = RestAPI.models.Game.objects.filter(name=name2)
    game1_json = json.loads(serializers.serialize('json', game1))
    game2_json = json.loads(serializers.serialize('json', game2))

    game1 = game1_json[0]['fields']
    game2 = game2_json[0]['fields']

    N = 2
    ind = np.arange(N)
    width = 0.1

    xvals = [game1['NA_Sales'], game2['NA_Sales']]
    bar1 = plt.bar(ind, xvals, width, color='r')

    yvals = [game1['EU_Sales'], game2['EU_Sales']]
    bar2 = plt.bar(ind + width, yvals, width, color='g')

    zvals = [game1['JP_Sales'], game2['JP_Sales']]
    bar3 = plt.bar(ind + width * 2, zvals, width, color='b')

    wvals = [game1['Other_Sales'], game2['Other_Sales']]
    bar4 = plt.bar(ind + width * 3, wvals, width, color='yellow')

    kvals = [game1['Global_Sales'], game2['Global_Sales']]
    bar5 = plt.bar(ind + width * 4, kvals, width, color='hotpink')

    plt.xlabel("name")

    plt.xticks(ind + width, [name1, name2])
    plt.legend((bar1, bar2, bar3, bar4, bar5), ('NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales'))
    plt.savefig('DataAnalysis/result/compareSales'+name1+'_'+name2+'.png')

    return HttpResponse(200)

@csrf_exempt
def compareSalesByYear(request):
    year1 = int(request.POST.get('year1'))
    year2 = int(request.POST.get('year2'))
    totals = []
    for i in range(year1, year2+1):
        yearGames = RestAPI.models.Game.objects.filter(year=i).aggregate(Sum('Global_Sales'))
        if yearGames['Global_Sales__sum'] == None:
            totals.append(0)
        else:
            totals.append(yearGames['Global_Sales__sum'])


    years = [x for x in range(year1, year2+1)]
    fig = plt.figure(figsize=(10, 5))
    plt.bar(years, totals, color='purple', width=0.4)

    plt.xlabel("years")
    plt.ylabel("Total sales")
    plt.savefig('DataAnalysis/result/compareSalesByYear.png')

    return HttpResponse(200)

@csrf_exempt
def comparePublisherSales(request):
    year1 = int(request.POST.get('year1'))
    year2 = int(request.POST.get('year2'))
    publisher1 = request.POST.get('publisher1')
    publisher2 = request.POST.get('publisher2')
    years = [x for x in range(year1, year2 + 1)]
    totals1 = [0 for x in range(year1, year2 + 1)]
    totals2 = [0 for x in range(year1, year2 + 1)]
    for i in range(year1, year2+1):
        publisher1_yearGames = RestAPI.models.Game.objects.filter(year=i, publisher=publisher1).aggregate(Sum('Global_Sales'))
        if publisher1_yearGames['Global_Sales__sum'] is not None:
            totals1[i-year1] = publisher1_yearGames['Global_Sales__sum']

        publisher2_yearGames = RestAPI.models.Game.objects.filter(year=i, publisher=publisher2).aggregate(Sum('Global_Sales'))
        if publisher2_yearGames['Global_Sales__sum'] is not None:
            totals2[i-year1] = publisher2_yearGames['Global_Sales__sum']

    plt.plot(years, totals1, label=publisher1)
    plt.plot(years, totals2, label=publisher2)
    plt.legend()
    plt.savefig('DataAnalysis/result/comparePublisherSales.png')
    return HttpResponse(200)

@csrf_exempt
def compareSalesByGenre(request):
    year1 = int(request.POST.get('year1'))
    year2 = int(request.POST.get('year2'))
    genres = RestAPI.models.Game.objects.all().values_list('genre', flat=True).distinct()
    totals = {}

    for i in range(0, len(genres)):
        totals[genres[i]] = []
    for i in range(year1, year2 + 1):
        for genre in genres:
            yearGames = RestAPI.models.Game.objects.filter(year=i, genre=genre).aggregate(Sum('Global_Sales'))
            if yearGames['Global_Sales__sum'] == None:
                totals[genre].append(0)
            else:
                totals[genre].append(yearGames['Global_Sales__sum'])
    x = []
    for genre in genres:
        x.append(sum(totals[genre]))

    plt.title(str(year1)+' to '+str(year2))
    plt.bar(list(genres), x, color='pink', width=0.25)
    plt.xlabel("Genres")
    plt.ylabel("Totals")
    plt.xticks(rotation=90)
    plt.savefig(f'DataAnalysis/result/compareSalesByGenre{year1}to{year2}.png')

    return HttpResponse(200)