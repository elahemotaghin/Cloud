from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import  csrf_exempt
from .models import Game
import json

@csrf_exempt
def gameInformation(request):
    rank = request.POST.get('rank')
    game = Game.objects.filter(rank=rank)
    game_serialized = serializers.serialize('json', game)
    game_json = json.loads(game_serialized)
    data = json.dumps(game_json)
    return HttpResponse(data)

@csrf_exempt
def searchByName(request):
    name = request.POST.get('name')
    game = Game.objects.filter(name__contains=name)
    game_serialized = serializers.serialize('json', game)
    game_json = json.loads(game_serialized)
    data = json.dumps(game_json)
    return HttpResponse(data)

@csrf_exempt
def bestGamesByPlatform(request):
    n = request.POST.get('n')
    platform = request.POST.get('platform')
    allGames = Game.objects.filter(platform=platform).all()[:int(n)]
    game_serialized = serializers.serialize('json', allGames)
    game_json = json.loads(game_serialized)
    data = json.dumps(game_json)
    return HttpResponse(data)

@csrf_exempt
def bestGamesByYear(request):
    n = request.POST.get('n')
    year = request.POST.get('year')
    allGames = Game.objects.filter(year=year).all()[:int(n)]
    game_serialized = serializers.serialize('json', allGames)
    game_json = json.loads(game_serialized)
    data = json.dumps(game_json)
    return HttpResponse(data)

@csrf_exempt
def bestGamesByGenre(request):
    n = request.POST.get('n')
    genre = request.POST.get('genre')
    allGames = Game.objects.filter(genre=genre).all()[:int(n)]
    game_serialized = serializers.serialize('json', allGames)
    game_json = json.loads(game_serialized)
    data = json.dumps(game_json)
    return HttpResponse(data)

@csrf_exempt
def best5GamesBySale(request):
    year = request.POST.get('year')
    platform = request.POST.get('platform')
    allGames = Game.objects.filter(year=year , platform=platform).all().order_by('-Global_Sales')[:5]
    game_serialized = serializers.serialize('json', allGames)
    game_json = json.loads(game_serialized)
    data = json.dumps(game_json)
    return HttpResponse(data)

@csrf_exempt
def compareBySale(request):
    allGames = Game.objects.all()
    filterGames = []
    for game in allGames:
        if game.EU_Sales > game.NA_Sales:
            filterGames.append(game)
    game_serialized = serializers.serialize('json', filterGames)
    game_json = json.loads(game_serialized)
    data = json.dumps(game_json)
    return HttpResponse(data)