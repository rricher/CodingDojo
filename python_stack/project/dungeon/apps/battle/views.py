from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Goblin, Slime, Log
from ..user.models import User
from ..character.models import Character, Ability
import random

floor1 = {
    'room1': [Goblin.objects.create()],
    'room2': [Slime.objects.create(name="Slime1"), Slime.objects.create(name="Slime2")],
    'room3': [Goblin.objects.create(name="Goblin1"), Goblin.objects.create(name='Goblin2')],
    'room4': [Goblin.objects.create(name="Goblin1"), Slime.objects.create(name='Goblin2'), Slime.objects.create()],
    'room5': [Goblin.objects.create(name='Lil Gobi', max_hp=50, hp=50, damage_min=5, damage_max=13, exp=25)]
}

class Intro(View):
    def get(self, request):
        monsters = floor1['room1']
        request.session['room'] = "room1"
        request.session['monsters'] = monsters
        request.session['round'] = 1
        request.session['log'] = []
        context = {
            'character': Character.objects.get(id=request.session['charid']),
            'monster': monsters[0].name,
        }
        return render(request, 'intro.html', context)
    def post(self, request):
        return redirect('/battle/')

class Battle(View):
    def get(self, request):
        character = Character.objects.get(id=request.session['charid'])
        context = {
            'char': character,
        }
        return render(request, 'battle.html', context)


class Attack(View):
    def post(self, request):
        request.session['log'] = []
        log = [f"Round {request.session['round']}"]
        char = Character.objects.get(id=request.session['charid'])
        ability = Ability.objects.get(id=request.post['abilid'])
        char_dmg = random.randint(ability[0].damage_min, ability[0].damage_max)
        monsters = request.session['monsters']
        attacked = request.session['attacked']
        mon_dmg = 0
        if monsters[attacked].hp - char_dmg > 0:
            monsters[attacked].hp -= char_dmg
            log.append(f"{char.name} {ability.name}s a {monster[attacked].name} for {char_dmg} points of damage")
            monsters[attacked].save()
        else:
            log.append(f"{char.name} has killed {monsters[attacked].name}")
            monsters.pop(attacked)
        if len(monsters) == 0:
            return redirect('/battle/cleared/')
        for monster in monsters:
            mon_dmg += random.randint(monster.damage_min, monster.damage_max)
            Log.objects.create(log=f"A {monster.name} hits you for {mon_dmg} points of damage", round=round)
        if mon_hp - char.hp < 1:
            char.hp = 0
            return redirect("/battle/death/")
        else:
            char.hp = char.hp - mon_dmg
        char.save()
        request.session['log'] = log
        request.session['round'] ++
        request.session['monsters'] = monsters
        return redirect('/battle/')

class Attacked(View):
    def post(self, request):
        request.session['attacked'] = request.post['attacked']
        char = Character.objects.get(id=request.session['charid'])
        abilities = char.chosen_class.abilities.filter(level_req <= char.level)
        return render(request, "attacked.html", {"abilities": abilities})

class Cleared(View):
    def get(self, request):
        monsters = floor1[request.session['room']]
        exp = 0
        char = Character.objects.get(id=request.session['charid'])
        for monster in monsters:
            exp += monster.exp
        char.exp += exp
        if char.level == 1:
            if char.exp > 10:
                char.level = 2
                char.exp -= 10
        if char.level == 2:
            if char.exp > 20:
                char.level = 3
                char.exp -= 20
        if char.level == 1:
            if char.exp > 30:
                char.level = 4
                char.exp -= 30
        if char.level == 1:
            if char.exp > 40:
                char.level = 5
                char.exp -= 40
        if char.level == 1:
            if char.exp > 50:
                char.level = 6
                char.exp -= 50
        room = request.session['room']
        room_num = int(room[len(room) - 1])
        room_num1 = room_num + 1
        room.replace(str(room_num), str(room_num1))
        monsters = floor1[room]
        request.session['room'] = room
        request.session['monsters'] = monsters
        request.session['round'] += 1
        request.session['log'] = []
        return redirect('/battle/')

class Death(View):
    request.session.clear()
    return redirect("")