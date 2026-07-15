from flask import Flask, render_template, redirect, url_for, session, request
import mysql.connector

app = Flask(__name__)

Hathaway = ["継続して見せる", "ゲームも", "勉強も", "筋トレも", "ウォーキングも"]

@app.route("/")
def index():
    #if not in session:
    #    return redirect(url_for("login"))

    conn = mysql.connector.connect(
        host = "localhost",
        user = "ms",
        db = "expense_tracker",
        password = ""
    )

    cursor = conn.cursor()

    sql = "SELECT * FROM expenses"

    cursor.execute(sql)

    tasks = cursor.fetchall()

    conn.close()


    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "ms",
        db = "expense_tracker",
        password = ""
    )

    cursor = conn.cursor()

    title = request.form["title"]
    amount = request.form["amount"]
    category = request.form["category"]
    
    sql = "INSERT INTO expenses (title, amount, category, user_id) VALUES (%s, %s, %s, 1)"

    cursor.execute(sql, (title, amount, category,))
    conn.commit()
    conn.close()

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=5000, debug=True)
