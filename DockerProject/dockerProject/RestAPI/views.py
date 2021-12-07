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
def bestGamesByPlatform(request):
    n = request.POST.get('n')
    platform = request.POST.get('platform')
    allGames = Game.objects.filter(platform=platform).all()[:int(n)]
    game_serialized = serializers.serialize('json', allGames)
    game_json = json.loads(game_serialized)
    data = json.dumps(game_json)
    return HttpResponse(data)
