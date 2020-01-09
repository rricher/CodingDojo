from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "This is my key"

@app.route("/")
def home():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1

    if 'count' not in session:
        session['count'] = 1

    if 'iter' in session:
        session['count'] += session['iter']
    else:
        session['itter'] = 1
        session['count'] += session['iter']

    if 'reset' in session:
        if session['reset'] == True:
            session['count'] = 1
            session['iter'] = 1
            session['reset'] = False
    else:
        session['reset'] = False

    return render_template("index.html", visits = session['visits'], count = session['count'], iter = session['iter'])

@app.route("/post", methods=["POST"])
def return_info():
    print(request.form)
    print(session)
    if 'reset' in request.form:
        session['reset'] = True
    if request.form['added'] != '':
        session['iter'] = int(request.form['added'])
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)