from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/play")
def play():
    return render_template("index.html", play = True)

@app.route("/play/<int:times>")
def playx(times):
    return render_template("index.html", playx = True, x = times)

@app.route("/play/<int:times>/<color>")
def playCol(times, color):
    return render_template("index.html", playCol = True, x = times, col = color)

if __name__ == "__main__":
    app.run(debug = True)