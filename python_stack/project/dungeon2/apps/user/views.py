from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import LoginForm, RegistrationForm
from .models import User
from ..character.models import ClassType, Ability
from django.contrib import messages
import bcrypt

class Index(View):
    def get(self, request):
        return redirect("/login/")

class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", {'form':form})

    def post(self, request):
        users = User.objects.filter(username=request.POST['username'])
        if users:
            user = users[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                    request.session['userid'] = user.id
                    return redirect('/character/select/')
        messages.error(request, "Invalid email or password")
        return redirect('/login/')

class Register(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'register.html', {'form':form})

    def post(self, request):
        fail = False
        if len(User.objects.filter(username=request.POST['username'])) > 0:
            fail = True
            messages.error(request, 'username is invalid')
        if len(request.POST['username']) < 3:
            fail = True
            messages.error(request, 'username must be longer than 3 chacters')
        if len(request.POST['password']) < 8:
            fail = True
            messages.error(request, 'password must be longer than 8 characters')
        if not request.POST['password'] == request.POST['confirm_password']:
            fail = True
            messages.error(request, 'passwords musth match')
        print(messages)
        if fail:
            return redirect('/register/')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(username=request.POST['username'], password=pw_hash)
            request.session['userid'] = user.id
            messages.success(request, "Successfuly registered")
            return redirect('/login/')

class Logout(View):
    def get(self, request):
        request.session.clear()
        return redirect('/login/')

class CreateDB(View):
    def get(self, request):
        warrior = ClassType.objects.create(name="Warrior", start_hp=30)
        rogue = ClassType.objects.create(name="Rogue", start_hp=25)
        wizard = ClassType.objects.create(name="Wizard", start_hp=20)
        Ability.objects.create(name="Slash", damage_min=3, damage_max=5, crit_chance=5, hit_chance=50, level_req=1, for_class=warrior)
        Ability.objects.create(name="Bash", damage_min=4, damage_max=10, crit_chance=10, hit_chance=70, level_req=3, for_class=warrior)
        Ability.objects.create(name="Stab", damage_min=1, damage_max=3, crit_chance=20, hit_chance=60, level_req=1, for_class=rogue)
        Ability.objects.create(name="Backstab", damage_min=4, damage_max=7, crit_chance=25, hit_chance=60, level_req=3, for_class=rogue)
        Ability.objects.create(name="Zap", damage_min=5, damage_max=5, crit_chance=0, hit_chance=90, level_req=1, for_class=wizard)
        Ability.objects.create(name="Fireball", damage_min=10, damage_max=10, crit_chance=0, hit_chance=90, level_req=3, for_class=wizard)
        return redirect('/login/')