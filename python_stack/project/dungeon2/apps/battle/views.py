from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Monster
from ..user.models import User
from ..character.models import Character, Ability
import random

class Floor(View):
    def get(self, request):
        # slime: _type="Slime", name='Slime', max_hp=15, hp=15, damage_min=1, damage_max=2, exp=3
        # goblin: _type="Goblin", name='Goblin', max_hp=20, hp=20, damage_min=2, damage_max=4, exp=5
        # change to ids instead of actual model objects
        mon1 = Monster.objects.create(_type="Goblin", name='Goblin', max_hp=20, hp=20, damage_min=2, damage_max=4, exp=5)
        mon2 = Monster.objects.create(_type="Slime", name="Slime1", max_hp=15, hp=15, damage_min=1, damage_max=2, exp=3)
        mon3 = Monster.objects.create(_type="Slime", name="Slime2", max_hp=15, hp=15, damage_min=1, damage_max=2, exp=3)
        mon4 = Monster.objects.create(_type="Goblin", name="Goblin1", max_hp=20, hp=20, damage_min=2, damage_max=4, exp=5)
        mon5 = Monster.objects.create(_type="Goblin", name='Goblin2', max_hp=20, hp=20, damage_min=2, damage_max=4, exp=5)
        mon6 = Monster.objects.create(_type="Goblin", name="Goblin1", max_hp=20, hp=20, damage_min=2, damage_max=4, exp=5)
        mon7 = Monster.objects.create(_type="Goblin", name='Goblin2', max_hp=20, hp=20, damage_min=2, damage_max=4, exp=5)
        mon8 = Monster.objects.create(_type="Slime", name='Slime', max_hp=15, hp=15, damage_min=1, damage_max=2, exp=3)
        mon9 = Monster.objects.create(_type="Goblin", name='Lil Gobi', max_hp=50, hp=50, damage_min=5, damage_max=13, exp=25)
        request.session['floor1'] = {
            'room1': [mon1.id],
            'room2': [mon2.id,  mon3.id],
            'room3': [mon4.id, mon5.id],
            'room4': [mon6.id, mon7.id, mon8.id],
            'room5': [mon9.id],
        }
        print(request.session['floor1'])
        return redirect("/battle/intro/")

class Intro(View):
    def get(self, request):
        if 'floor1' not in request.session:
            return redirect("/battle/floor/")
        print(request.session['floor1'])
        monsters = request.session['floor1']['room1']
        request.session['room'] = "room1"
        request.session['monsters'] = monsters
        print(request.session['monsters'])
        request.session['round'] = 1
        request.session['log'] = []
        request.session['defeted'] = []
        monster = Monster.objects.get(id=monsters[0])
        char = Character.objects.get(id=request.session['charid'])
        char.hp = char.max_hp
        char.save()
        context = {
            'character': char,
            'monster': monster,
        }
        return render(request, 'intro.html', context)

    def post(self, request):
        return redirect('/battle/')

class Battle(View):
    def get(self, request):
        character = Character.objects.get(id=request.session['charid'])
        monsters_ids = request.session['monsters']
        monsters = []
        for monster in monsters_ids:
            monsters.append(Monster.objects.get(id=monster))
        context = {
            'char': character,
            'monsters': monsters,
        }
        return render(request, 'battle.html', context)


class Attack(View):
    def post(self, request):
        request.session['log'] = []
        log = [f"Round {request.session['round']}"]
        char = Character.objects.get(id=request.session['charid'])
        ability = Ability.objects.get(id=int(request.POST['abilid']))
        modifier = 1
        crit = random.randint(1, 100)
        if ability.crit_chance > crit:
            modifier = 2
        char_dmg = random.randint(ability.damage_min, ability.damage_max) * modifier
        monsters_ids = request.session['monsters']
        monsters = []
        attacked_i = int(request.session['attacked'])
        for monster in monsters_ids:
            monsters.append(Monster.objects.get(id=monster))
        attacked = monsters[attacked_i]
        mon_dmg = 0
        print(attacked)
        if attacked.hp - char_dmg > 0:
            attacked.hp -= char_dmg
            log.append(f"{char.name} {ability.name}s a {attacked.name} for {char_dmg} points of damage")
            attacked.save()
        else:
            log.append(f"{char.name} has killed {attacked.name}")
            request.session['defeted'].append(attacked.id)
            attacked.hp = 0
            attacked.save()
        if monsters_ids == request.session['defeted']:
            return redirect('/battle/cleared/')
        for monster in monsters:
            dmg = random.randint(monster.damage_min, monster.damage_max)
            mon_dmg += dmg
            log.append(f"{monster.name} has hit you for {dmg} points of damage")
            print(mon_dmg)
        if char.hp - mon_dmg < 1:
            char.hp = 0
            return redirect("/battle/death/")
        else:
            char.hp = char.hp - mon_dmg
        char.save()
        request.session['log'] = log
        request.session['round'] += 1
        request.session['monsters'] = monsters_ids
        return redirect('/battle/')

class Attacked(View):
    def post(self, request):
        print("made it to attacked \ "*5)
        print(request.POST)
        request.session['attacked'] = request.POST['attacked']
        char = Character.objects.get(id=request.session['charid'])
        print(char.chosen_class.abilities.all().values())
        print(char.level)
        abilities = char.chosen_class.abilities.filter(level_req__lte = char.level)
        print(abilities[0])
        return render(request, "attacked.html", {"abilities": abilities})

class Cleared(View):
    def get(self, request):
        monster_ids = request.session['defeted']
        print(monster_ids)
        exp = 0
        char = Character.objects.get(id=request.session['charid'])
        for monster in monster_ids:
            exp += Monster.objects.get(id=monster).exp
        char.exp += exp
        if char.level == 1:
            if char.exp > 10:
                char.level = 2
                char.exp -= 10
                char.max_hp += 5
        if char.level == 2:
            if char.exp > 20:
                char.level = 3
                char.exp -= 20
                char.max_hp += 5
        if char.level == 1:
            if char.exp > 30:
                char.level = 4
                char.exp -= 30
                char.max_hp += 5
        if char.level == 1:
            if char.exp > 40:
                char.level = 5
                char.exp -= 40
                char.max_hp += 5
        if char.level == 1:
            if char.exp > 50:
                char.level = 6
                char.exp -= 50
                char.max_hp += 5
        char.hp = char.max_hp
        char.save()
        found = False
        end = True
        print("monsters before ",request.session['monsters'])
        print(request.session['floor1'])
        for k in request.session['floor1']:
            print(request.session['floor1'][k])
            if found:
                end = False
                request.session['room'] = k
                break
            if request.session['floor1'][k] == request.session["monsters"]:
                found = True
        print(request.session['room'])
        request.session["monsters"] = request.session['floor1'][request.session['room']]
        print("monsters after ",request.session['monsters'])
        request.session['round'] = 0
        request.session['log'] = []
        request.session['defeted'] = []
        if end:
            return redirect("/battle/intro/")
        return redirect('/battle/')

class Death(View):
    def get(self, request):
        request.session.clear()
        return redirect("/login/")