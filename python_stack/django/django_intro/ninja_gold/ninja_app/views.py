from django.shortcuts import render, redirect
import random

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'message' not in request.session:
        request.session['message'] = []
    context = {
        'gold': request.session['gold'],
        'messages': request.session['message'],
    }
    return render(request, 'index.html', context)

def process_money(request, building):
    print(building)
    print(request.session['gold'], request.session['message'])
    if request.method == 'GET':
        if building == 'farm':
            gold = random.randint(10, 20)
            request.session['gold'] += gold
            request.session['message'].append(f"<li style='color: green;'>Earned {gold} from the Farm</li>")
        if building == 'cave':
            gold = random.randint(5, 10)
            request.session['gold'] += gold
            request.session['message'].append(f"<li style='color: green;'>Earned {gold} from the Cave</li>")
        if building == 'house':
            gold = random.randint(2, 5)
            request.session['gold'] += gold
            request.session['message'].append(f"<li style='color: green;'>Earned {gold} from the House</li>")
        if building == 'cassino':
            gold = random.randint(-50, 50)
            request.session['gold'] += gold
            if gold >= 0:
                request.session['message'].append(f"<li style='color: green;'>Earned {gold} from the cassino</li>")
            else:
                request.session['message'].append(f"<li style='color: red;'>Lost {gold * -1} from the cassino</li>")
        request.session.save()
    return redirect("/")