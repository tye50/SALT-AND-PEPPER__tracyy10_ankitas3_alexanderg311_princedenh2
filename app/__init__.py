from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for
from flask import flash
import os
import numpy as np 
import pandas as pd
import random

import sqlite3
import db

import news_analysis

app = Flask(__name__)
secret = os.urandom(32)
app.secret_key = secret

@app.route("/")
def main():
    if 'username' in session:
        return redirect("/dashbord")
    return render_template("main.html")

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