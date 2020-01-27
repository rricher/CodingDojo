from django.shortcuts import render, redirect
from django.views.generic import View

class Index(View):
    def get(self, request):
        return redirect("/login/")

class Login(View):
    def get(self, request):
        return render(request, "login.html")

class Register(View):
    def get(self, request):
        return render(request, 'register.html')