from django.shortcuts import render
from datetime import datetime

def index(request):
    time = datetime.now()
    context = {
        'date': time.strftime("%b %d, %Y"),
        'time': time.strftime("%I:%M %p"),
    }
    return render(request, 'index.html', context)
