from django.shortcuts import render
from .models import *
import json
from django.http import *
# Create your views here.

def api_dice(request):
    dice = [4, 6, 8, 10, 12, 20]
    output = json.dumps(dice)
    return HttpResponse(output, content_type="application/json")

def api_dice_roll(request, number):
    die = Die()
    die.name = "d" + number
    die.number = int(number)
    result = die.roll()
    result_dict = {"result": result}
    output = json.dumps(result_dict)
    return HttpResponse(output, content_type="application/json")

def index(request):
    return render(request,"index.html", {})

def player_character_selection(request):
    return render(request,"index.html", {})
