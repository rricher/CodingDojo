from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "this is a verry seceret key"

@app.route("/", methods=['GET', 'POST'])
def home():
    session['random'] = random.randint(1, 100)
    session['above'] = False
    session['bellow'] = False
    session['correct'] = False
    return render_template("index.html")

@app.route("/post", methods=['POST'])
def post():
    if int(request.form['guess']) > session['random']:
        session['above'] = True
        session['bellow'] = False
        session['correct'] = False
        return render_template("index.html")
    if int(request.form['guess']) < session['random']:
        session['above'] = False
        session['bellow'] = True
        session['correct'] = False
        return render_template("index.html")
    else:
        session['above'] = False
        session['bellow'] = False
        session['correct'] = True
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)