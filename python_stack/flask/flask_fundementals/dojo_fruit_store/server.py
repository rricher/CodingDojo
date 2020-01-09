from flask import Flask, render_template, request, redirect
app = Flask(__name__)
from datetime import datetime

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    straw = request.form['strawberry']
    apple = request.form['apple']
    rasp = request.form['raspberry']
    total = int(apple) + int(straw) + int(rasp)
    last = request.form['last_name']
    first = request.form['first_name']
    stud_id = request.form['student_id']
    date_time = datetime.now()
    time = date_time.strftime("%B %d %Y %I:%M:%S %p")
    print(f"Charging {first} {last} for {total} fruits")
    return render_template("checkout.html", straw = straw, rasp = rasp, apple = apple, total = total, first = first, last = last, stud_id = stud_id, time = time)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    