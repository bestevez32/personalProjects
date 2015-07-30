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
    dice = [ ]

    d4 = Die()
    d4.name = 'd4'
    d4.number = 4
    dice.append(d4)

    d6 = Die()
    d6.name = 'd6'
    d6.number = 6
    dice.append(d6)

    d8 = Die()
    d8.name = 'd8'
    d8.number = 8
    dice.append(d8)

    d10 = Die()
    d10.name = 'd10'
    d10.number = 10
    dice.append(d10)

    d12 = Die()
    d12.name = 'd12'
    d12.number = 12
    dice.append(d12)

    d20 = Die()
    d20.name = 'd20'
    d20.number = 20
    dice.append(d20)

    roll = d10.roll()

    return render(request,"index.html", {"roll": roll, "dice": dice})

