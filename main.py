from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/men')
def men():
    return render_template("men.html")


@app.route("/women")
def women():
    return render_template("women.html")

@app.route("/art")
def art():
    return render_template("art.html")

@app.route("/payment")
def payment():
    return render_template("payment.html")



@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)