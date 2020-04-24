from flask import Flask, render_template, request
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


@app.route("/dL")
def show_dynamic():
    return render_template('duplicate_layout.html')


@app.route("/form")
def show_form():
    return render_template("form.html")


@app.route("/fR", methods=["POST", "GET"])
def show_form_result():
    if request.method == "GET":
        return "GET method is called"
    else:
        name = request.form.get("name")
        return render_template('duplicate_layout.html', name=name)


lists = []


@app.route("/exS", methods=["GET", "POST"])
def store_session():
    item = request.form.get("item")
    lists.append(item)
    return render_template("session.html", lists=lists)


if __name__ == '__main__':
    app.run()
