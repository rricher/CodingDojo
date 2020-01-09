from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<name>")
def say(name):
    return f"Hi {name}"

@app.route("/repeat/<int:num>/<phrase>")
def repeat(num, phrase):
    return f"{phrase} " * num

@app.route("/<path:other>")
def errorPath(other):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug = True)