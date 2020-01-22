from django.shortcuts import render, redirect
from .models import *

def books(request):
    if request.method == 'GET':
        context = {
            'books': Book.objects.all(),
        }
        return render(request, 'books.html', context)

    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Book.objects.create(title=title, description=description)
        return redirect('/')

def authors(request):
    if request.method == 'GET':
        context = {
            'authors': Author.objects.all(),
        }
        return render(request, 'authors.html', context)

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        notes = request.POST['notes']
        Author.objects.create(first_name=first_name, last_name=last_name, notes=notes)
        return redirect('/authors')

def show_book(request, id):
    if request.method == 'GET':
        context = {
            'book': Book.objects.get(id=id),
            'authors': Author.objects.all(),
        }
        return render(request, 'show_book.html', context)

    if request.method == 'POST':
        if 'author_id' in request.POST:
            book = Book.objects.get(id=id)
            author = Author.objects.get(id=request.POST['author_id'])
            book.authors.add(author)
        return redirect(f'/books/{id}')

def show_author(request, id):
    if request.method == 'GET':
        context = {
            'author': Author.objects.get(id=id),
            'books': Book.objects.all(),
        }
        return render(request, 'show_author.html', context)

    if request.method == 'POST':
        if 'book_id' in request.POST:
            author = Author.objects.get(id=id)
            book = Book.objects.get(id=request.POST['book_id'])
            author.books.add(book)
        return redirect(f'/authors/{id}')







