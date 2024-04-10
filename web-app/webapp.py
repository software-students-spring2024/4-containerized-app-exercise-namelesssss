from flask import Flask, render_template, request, redirect, abort, url_for, make_response

app = Flask(__name__)

@app.route('/', methods=["POST"])
def home():
    if request.method == "POST":
        inputText = request.form.get("inputText")

    return render_template("home.html")

if __name__ =="__main__":
    app.run()