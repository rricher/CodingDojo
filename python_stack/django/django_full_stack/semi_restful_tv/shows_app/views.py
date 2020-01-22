from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show

def index(request):
    return redirect("/shows")

def shows(request):
    context = {
        'shows': Show.objects.all(),
    }
    return render(request, 'shows.html', context)

def new(request):
    if request.method == 'GET':
        return render(request, 'new.html')
    if request.method == 'POST':
        # pass the post data to the method we wrote and save the response in a variable called errors
        errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            # redirect the user back to the form to fix the errors
            return redirect('/shows/new')
        else:
            new_show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
            return redirect(f"/shows/{new_show.id}")

def show_id(request, id):
    context = {
        'show': Show.objects.get(id=id),
    }
    return render(request, 'show_id.html', context)

def edit(request, id):
    if request.method == 'GET':
        context = {
            'show': Show.objects.get(id=id),
        }
        return render(request, 'edit.html', context)
    if request.method == 'POST':
        # pass the post data to the method we wrote and save the response in a variable called errors
        errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            # redirect the user back to the form to fix the errors
            id = int(request.POST['id'])
            return redirect(f'/shows/{id}/edit')
        else:
            show = Show.objects.get(id=int(request.POST['id']))
            show.title = request.POST['title']
            show.network = request.POST['network']
            show.release_date = request.POST['release_date']
            show.description = request.POST['description']
            show.save() 
            return redirect(f"/shows/{show.id}")

def delete(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect("/shows")