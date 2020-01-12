from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = "this is a verry secret key"

@app.route("/")
def home():
    if 'gold' not in session:
        session['gold'] = 0
    if 'message' not in session:
        session['message'] = []
    return render_template("index.html")

@app.route("/process_money", methods=['POST'])
def process():
    print(request.form)
    print(session)
    if request.form['building'] == 'farm':
        gold = random.randint(10, 20)
        session['gold'] += gold
        session['message'].append(f"<li style='color: green;'>Earned {gold} from the Farm</li>")
    if request.form['building'] == 'cave':
        gold = random.randint(5, 10)
        session['gold'] += gold
        session['message'].append(f"<li style='color: green;'>Earned {gold} from the Cave</li>")
    if request.form['building'] == 'house':
        gold = random.randint(2, 5)
        session['gold'] += gold
        session['message'].append(f"<li style='color: green;'>Earned {gold} from the House</li>")
    if request.form['building'] == 'cassino':
        gold = random.randint(-50, 50)
        session['gold'] += gold
        if gold >= 0:
            session['message'].append(f"<li style='color: green;'>Earned {gold} from the cassino</li>")
        else:
            session['message'].append(f"<li style='color: red;'>Lost {gold * -1} from the cassino</li>")
        session.modified = True
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)