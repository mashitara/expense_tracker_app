from flask import Flask, render_template, redirect, url_for, session
import mysql.connector

app = Flask(__name__)

Hathaway = ["継続して見せる", "ゲームも", "勉強も", "筋トレも", "ウォーキングも"]

@app.route("/")
def index():
    if not in session:
        return redirect(url_for("login"))

    conn = mysql.connector.connect(
        host = "localhost",
        user = "ms",
        db = "expense_tracker",
        password = ""
    )

    cursor = conn.cursor()

    sql = "SELECT * FROM exepenses"

    cursor.execute(sql)

    tasks = cursor.fetchall()

    conn.close()


    return render_template("index.html", tasks=tasks)