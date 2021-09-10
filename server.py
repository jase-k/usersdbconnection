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
    id = User.addUser(data)
    return redirect(f'/users/{id}')

@app.route('/users/<int:id>')
def showUser(id):
    user = User.getUserById(id)
    print("User Data: ", user)
    return render_template("show_user.html", user = user)

@app.route('/users/<int:id>/edit')
def editUser(id):
    user = User.getUserById(id)
    return render_template("edit_user.html", user = user)

@app.route('/users/<int:id>/edit_submit', methods=["POST"])
def editUserSubmit(id):
    #Code to submit edits to the database here
    data = {
        "id" : id, 
        "fname" : request.form['fname'],
        "lname" : request.form['lname'],
        "email" : request.form['email']
    }
    print("The new informaiton for user is: ", data)
    User.updateUser(data)
    return redirect(f'/users/{id}')

@app.route('/users/<int:id>/delete')
def delete(id):
    User.deleteUser(id)
    return redirect('/')

if(__name__ == "__main__"):
    app.run(debug=True)