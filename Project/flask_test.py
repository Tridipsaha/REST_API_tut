from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/tridip")
def tridip():
    return "Hello World Tridip!"


@app.route("/about")
def tridips():
    return render_template('index.html')

app.run(debug= True)