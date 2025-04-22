from flask import Flask, render_template, session, redirect, url_for, flash, request
import os
import random
import csv
import sqlite3
import news_classifier
import pickle
import news_scrape
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import shutil 

from db import *

app = Flask(__name__)
secret = os.urandom(32)
app.secret_key = secret

@app.route("/")
def main():
    if 'username' in session:
        return redirect("/dashboard")
    return render_template("main.html")

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        username=request.form.get("username")
        password=request.form.get("password")
        checkUser=getUser(username)
        if checkUser==0:
            flash("THIS ACCOUNT DOES NOT EXIST")
            return render_template("login.html")
        elif password!=checkUser[1]:
            flash("INCORRECT PASSWORD")
            return render_template("login.html")
        else:
            session['username'] = username
            return render_template("dashboard.html")
        
@app.route("/register", methods=['GET','POST'])
def register():
    if request.method=="GET":
        return render_template("register.html")
    else:
        username=request.form.get("username")
        password=request.form.get("password")
        if (attemptAddUser(username, password) == 0):
            session['username'] = username
            return render_template("dashboard.html")
        else:
            flash("THIS USERNAME IS TAKEN")
            return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    if not 'username' in session:
        flash("Please log in to access this page.")
        return redirect("/")
    return render_template("dashboard.html")


@app.route("/search", methods=['GET','POST'])
def search():
    if not 'username' in session:
         flash("Please log in to access this page.")
         return redirect("/")
    query = request.form.get("query")
    count = wordCountF(query)
    words = returnWordsF()

    countR = wordCountT(query)
    wordsR = returnWordsT()

    fake_or_real = np.array(["Fake", "Real"])
    values = np.array([count, countR])


    plt.bar(fake_or_real, values, color="black")
    plt.rcParams['font.family'] = 'Outfit' 
    plt.xlabel("True or False")
    plt.ylabel("Count")
    plt.title(query)
    plt.savefig('torf.png')
    shutil.move("./torf.png", "static/torf.png")
    plt.close()
    return render_template("search.html", query=query, count=count, words=words, countR=countR, wordsR=wordsR)

@app.route("/analyze", methods=['GET', 'POST'])
def analyze():
    if not 'username' in session:
        flash("Please log in to access this page.")
        return redirect("/")
    if request.method == 'POST':
        link = request.form['link']
        try:
            text = news_scrape.get_text(link)
            p = news_classifier.get_probability(model, text)
            return render_template("analyze.html", link=link, text=text, p_true=p[0],p_false=p[1])
        except Exception as e:
            print(e)
            flash('Invalid URL or unable to fetch the article. Please try again.')
            return render_template("analyze.html", link=None, text=None, p_true=None, p_false=None)
    return render_template("analyze.html",link=None, text=None, p_true=None, p_false=None)
    return render_template("analyze.html")

@app.route("/generate")
def generate():
    if not 'username' in session:
        flash("Please log in to access this page.")
        return redirect("/")
    
    return render_template("generate.html")

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect("/")
    
if __name__ == "__main__":
    app.debug = True
    model = pickle.load(open("finalized_model.sav", "rb"))
    news_classifier.fit_tfidf_vectorizer()
    print("Model loaded")
    app.run()