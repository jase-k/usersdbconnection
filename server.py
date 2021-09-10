from flask import Flask, render_template, request, redirect;
from users import User

app = Flask(__name__)

@app.route('/')
def index():
    print(User.getUsers())
    users = User.getUsers()
    return render_template("index.html", users = users)

@app.route('/users/new')
def addUserOptions():
    return render_template("add_user.html")

@app.route('/users/add_new', methods=["POST"])
def addUser():
    data = {
        "fname" : request.form['fname'],
        "lname" : request.form['lname'], 
        "email" : request.form['email']
    }
    print("data submitted: ", data)
    User.addUser(data)
    return redirect('/')

if(__name__ == "__main__"):
    app.run(debug=True)