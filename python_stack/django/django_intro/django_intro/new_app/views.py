from django.shortcuts import render, HttpResponse, redirect

def index(response):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(response):
    return HttpResponse("placeholder to later display a list of all blogs")

def create(resonse):
    return redirect('/')

def show(response, number):
    return HttpResponse(f"placeholder to display blog number {number}")

def edit(response, number):
    return HttpResponse(f"placeholder to edit blog number {number}")

def destroy(response, number):
    return redirect("/")