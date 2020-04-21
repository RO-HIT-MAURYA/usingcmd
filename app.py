from flask import Flask, render_template

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


if __name__ == '__main__':
    app.run()
