from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Character
from ..user.models import User

class CharacterSelect(View):
    def get(self, request):
        user = User.objects.get(id=request.session['userid'])
        characters = user.characters.all()
        return render(request, 'charselect.html', {'characters':characters})
    
    def post(self, request):
        print(request.POST)
        if request.POST['data'] == 'create':
            return redirect('/character/create/')

class CharacterCreate(View):
    def get(self, request):
        return render(request, 'charcreate.html')

    def post(self,request):
        return redirect('/character/')
