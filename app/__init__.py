from flask import Flask,render_template
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for
from flask import flash
import sqlite3
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")


if __name__ == "__main__":
    app.debug = True
    app.run()