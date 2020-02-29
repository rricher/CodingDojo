from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Character, ClassType
from ..user.models import User

class CharacterSelect(View):
    def get(self, request):
        user = User.objects.get(id=request.session['userid'])
        characters = user.characters.all()
        print(characters.values())
        return render(request, 'charselect.html', {'characters':characters})
    
    def post(self, request):
        print(request.POST)
        if request.POST['data'] == 'create':
            return redirect('/character/create/')
        else:
            request.session['charid'] = request.POST['data']
            return redirect('/battle/intro/')

class CharacterCreate(View):
    def get(self, request):
        return render(request, 'charcreate.html')

    def post(self,request):
        print(request.POST)
        user = User.objects.get(id=request.session['userid'])
        request.session['charname'] = request.POST['name']
        return redirect('/character/class/')

class SelectClass(View):
    def get(self, request):
        context = {
            "classess": ClassType.objects.all()
        }
        return render(request, "selectclass.html", context)

    def post(self,request):
        user = User.objects.get(id=request.session['userid'])
        name = request.session['charname']
        classType = ClassType.objects.get(id=request.POST['data'])
        hp = classType.start_hp
        char = Character.objects.create(name=name, chosen_class=classType, max_hp=hp, hp=hp)
        request.session['charid'] = char.id
        return redirect('/battle/intro/')
