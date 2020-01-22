from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User, Message, Comment
import bcrypt

def index(request):
    if request.method == "GET":
        if request.session.__contains__('userid'):
            return redirect('/wall')
        else:
            context = {
            }
            return render(request, 'index.html', context)
    if request.method == "POST":
        if request.POST['reg_or_log'] == "reg":
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
                return redirect('/wall')
        if request.POST['reg_or_log'] == "log":
            user = User.objects.filter(email=request.POST['email'])
            if user:
                logged_user=user[0]
                if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                    request.session['userid'] = logged_user.id
                    messages.success(request, "Successfuly registered (or logged in)!")
                    return redirect('/wall')
            messages.error(request, "Invalid email or password", extra_tags="login")
            return redirect('/')

def wall(request):
    if request.method == 'GET':
        context = {
            "user": User.objects.get(id = request.session['userid']),
            "messages": Message.objects.all().order_by('-created_at'),
        }
        return render(request, 'wall.html', context)
    if request.method == 'POST':
        print(request.POST['message'])
        return redirect('/wall')

def logout(request):
    request.session.clear()
    return redirect('/')

def post_message(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.POST['userid'])
        Message.objects.create(user=user, message=request.POST['message'])
        context = {
            "messages": Message.objects.all().order_by('-created_at'),
        }
        return render(request, 'partials/messages.html', context)

def post_comment(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.POST['userid'])
        message = Message.objects.get(id=request.POST['messageid'])
        Comment.objects.create(user=user, message=message, comment=request.POST['comment'])
        context = {
            "message": message
        }
        return render(request, 'partials/comments.html', context)