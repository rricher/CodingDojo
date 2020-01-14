from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    return redirect('/random_word')

def random_word(request):
    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1
    random = get_random_string(length=14)
    context = {
        'random': random
    }
    return render(request, "index.html", context)

def reset(request):
    del request.session['count']
    return redirect('/random_word')