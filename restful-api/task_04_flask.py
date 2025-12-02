#!/usr/bin/python3
"""Web app with flask"""
from flask import Flask
from flask import jsonify
from flask import request

users = {}
user_error = {"error": "User not found"}
user_exist = {"error":"Username already exists"}
user_req = {"error":"Username is required"}
invalid_json = {"error":"Invalid JSON"}

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Flask API!"
@app.route("/data")
def data():
    usernames = list(users.key())
    return jsonify(usernames)
@app.route("/status")
    return "OK"
@app.route("/users/<username>")
    if username in username:
        return "User valid"
    else:
        return jsonify(user_error), 404
@app.route("/add_user", methods = ["POST"])
    def add_user():
        new_user = request.get_json(silent=True)
        username = new_user.get("username")
        if new_user is None:
            return jsonify(invalid_json), 400
        if username == "":
            return jsonify(user_req), 400
        if username in usernames:
            return jsonify(user_exist), 409
        users[username] = new_user

if __name__ == "__main__":
    app.run()
