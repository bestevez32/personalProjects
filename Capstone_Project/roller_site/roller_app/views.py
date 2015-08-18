from django.shortcuts import render
from .models import *
import json
from django.http import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


@login_required(login_url='/login/')
def index(request):
    if request.POST:
        print(request.POST)
    return render(request, "index.html", {})


def login_view(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/")

    return render(request, 'login.html', {})


def register_view(request):
    if request.POST:
        user = User()
        user.username = request.POST['username']
        user.set_password(request.POST['password'])
        user.save()
        return HttpResponseRedirect("/login")

    return render(request, 'register.html', {})


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


def player_character_selection(request):
    return render(request, "index.html", {})


@csrf_exempt
def api_newCharacter(request):
    if request.POST:
        print(request.POST)
        id = int(request.POST["id"])
        if id > 0:
            pc = PlayerCharacter.objects.filter(id=id)[0]
        else:
            pc = PlayerCharacter()
        pc.character_name = request.POST['character_name']
        pc.save()
        for i in range(0, 5):
            pcv = PCValue()
            pcv.character = pc

            ability_id = int(request.POST["ability-" + str(i)])
            ability = Abilities.objects.filter(id=ability_id)[0]
            pcv.ability = ability

            die_value_id = int(request.POST["die_value-" + str(i)])
            die_value = AbilityValues.objects.filter(id=die_value_id)[0]
            pcv.die_value = die_value

            pcv.save()
        return HttpResponse(str(pc.id), content_type="application/json")

    character_list = PlayerCharacter.objects.all()
    output_list = []
    for c in character_list:
        pairs = PCValue.objects.filter(character = c)
        output_pairs = []
        for p in pairs:
            output_pairs.append({"ability": p.ability.id, "diceValue": p.die_value.id})
        output_list.append({"id": c.id, "name": c.character_name, "pairs": output_pairs})
    return HttpResponse(json.dumps(output_list, indent=4), content_type="application/json")


