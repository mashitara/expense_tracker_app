from flask import Flask, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

Hathaway = ["継続して見せる", "ゲームも", "勉強も", "筋トレも", "ウォーキングも"]

@app.route("/")
def index():
    if not in session:
        return redirect(url_for("login"))

    return render_template("index.html")