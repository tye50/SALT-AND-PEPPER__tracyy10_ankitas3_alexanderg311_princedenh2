from flask import Flask, render_template, session, redirect, url_for, flash, request
import os
import random
import csv
import sqlite3

from db import *

app = Flask(__name__)
secret = os.urandom(32)
app.secret_key = secret

@app.route("/")
def main():
    if 'username' in session:
        return redirect("/dashbord")
    words=[]
    for i in range(10):
        if random.choice([True, False]) == True:
            words.append(getRandomFakeWord())
        else:
            getRandomTrueWord()
    return render_template("main.html", words=words)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    if not 'username' in session:
        # add flash
        return redirect("/main")
    return render_template("dashboard.html")

@app.route("/search")
def search():
    if not 'username' in session:
        # add flash
        return redirect("/main")
    return render_template("search.html")

@app.route("/analyze")
def analyze():
    if not 'username' in session:
        # add flash
        return redirect("/main")
    return render_template("analyze.html")

@app.route("/generate")
def generate():
    if not 'username' in session:
        # add flash
        return redirect("/main")
    return render_template("generate.html")

if __name__ == "__main__":
    app.debug = True
    app.run()