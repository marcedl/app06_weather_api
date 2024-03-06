from flask import Flask #web framewrk is a manager for multiple pages 
from flask import render_template

#Create a website object
app = Flask("Website")

@app.route("/home") #decorator that connects to .html file
def home():
    return render_template("tutorial.html")
@app.route("/about") 
def about():
    return render_template("about.html")


app.run(debug=True)