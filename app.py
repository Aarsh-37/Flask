# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World this flask</p>"

# if __name__== "__main__":
#     app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")  # Assuming you have a file 'index.html' in the templates folder

@app.route("/products")
def products():
    return "<p>Hello, this is the product page</p>"

@app.route("/home")
def home_page():
    return "<p>Hello, this is the home page, tell me more about you</p>"

if __name__ == "__main__":
    app.run(debug=True, port=8000)
