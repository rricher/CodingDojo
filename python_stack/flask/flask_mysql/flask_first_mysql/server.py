from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
app = Flask(__name__)

@app.route('/')
def index():
    mysql = connectToMySQL("first_flask")
    friends = mysql.query_db("SELECT * FROM friends;")
    print(friends)
    return render_template("index.html", all_friends = friends)

@app.route("/create_friend", methods=["POST"])
def add_friend_to_db():
    mysql = connectToMySQL("first_flask")

    query = "INSERT INTO friends (first_name, last_name, occupation) VALUES (%(fn)s, %(ln)s, %(occp)s);"
    data = {
        "fn": request.form["fname"],
        "ln": request.form["lname"],
        "occp": request.form["occ"]
    }
    new_friend_id = mysql.query_db(query, data)
    return redirect("/")
    # QUERY: INSERT INTO first_flask (first_name, last_name, occupation, created_at, updated_at) 
    #                         VALUES (fname from form, lname from form, occupation from form, NOW(), NOW());

if __name__ == "__main__":
    app.run(debug=True)
