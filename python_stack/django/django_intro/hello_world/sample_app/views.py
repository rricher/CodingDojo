from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'index.html')

def hello_name(request, name):
    context = {
        'htmlname': name,
        'namelist': ['Alice', 'Bob', 'Ryan', 'Pete']
    }
    return render(request, 'helloname.html', context)