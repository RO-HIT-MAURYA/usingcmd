from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/rohit')
def show_name():
    return 'Hii rohit'


@app.route("/<string:name>")
def any_name(name):
    name = name.capitalize()
    return f"name is <H1>{name}<H1>"


@app.route("/rR")
def show_page():
    title = "titles"
    return render_template("demo.html", headline=title)


@app.route("/nY")
def check_new_year():
    now = datetime.datetime.now()
    ny = now.day == 1 and now.month == 1
    return render_template("demo.html", ny=ny)


@app.route("/name")
def show_list():
    names = ["rohit", "maurya"]
    return render_template("demo.html", names=names)


@app.route("/next")
def show_next():
    return render_template("next.html")


if __name__ == '__main__':
    app.run()
