from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result", methods=['POST'])
def response():
    name = request.form['name']
    dojo = request.form['dojo']
    lang = request.form['lang']
    return render_template("info.html", name = name, dojo = dojo, lang = lang)

if __name__ == "__main__":
    app.run(debug = True)