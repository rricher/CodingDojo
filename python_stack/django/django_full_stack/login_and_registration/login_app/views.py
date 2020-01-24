from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
import bcrypt

def index(request):
    if request.method == "GET":
        if request.session.__contains__('userid'):
            return redirect('/success')
        else:
            context = {
            }
            return render(request, 'index.html', context)
    if request.method == "POST":
        if request.POST['reg_or_log'] == "reg":
            if not "checked" in request.POST:
                print("checked is not present")
                messages.error(request, "please agree to the terms and conditions", extra_tags='register')
                return redirect("/")
            errors = User.objects.basic_validator(request.POST)
            if len(errors) > 0:
                for k, v in errors.items():
                    messages.error(request, v, extra_tags='register')
                print(messages.get_messages(request))
                return redirect('/')
            else: 
                password = request.POST['password']
                pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
                print(pw_hash)
                user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash)
                request.session['userid'] = user.id
                messages.success(request, "Successfuly registered (or logged in)!")
                return redirect('/success')
        if request.POST['reg_or_log'] == "log":
            user = User.objects.filter(email=request.POST['email'])
            if user:
                logged_user=user[0]
                if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                    request.session['userid'] = logged_user.id
                    messages.success(request, "Successfuly registered (or logged in)!")
                    return redirect('/success')
            messages.error(request, "Invalid email or password", extra_tags="login")
            return redirect('/')


def success(request):
    if request.session.__contains__('userid'):
        context ={
            "user_name": User.objects.get(id=request.session['userid']).first_name
        }
        return render(request, 'success.html', context)
    else:
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def email(request):
    if request.method == 'POST':
        print("got to email YAY!")
        check = User.objects.filter(email = request.POST['email'])
        print(check)
        context ={
            "found": False
        }
        if check:
            context['found'] = True
        print(render(request, "partials/email.html", context))
        return render(request, 'partials/email.html', context)