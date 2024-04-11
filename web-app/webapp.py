from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        input_text = request.form.get("inputText")
        response = requests.post("http://localhost:5000/analyze", json={"passage": input_text})
        if response.status_code == 200:
            result = response.json()
            return render_template("home.html", original_text=input_text, fixed_text=result["fixed_passage"], error_analysis=result["error_analysis"])
        else:
            return render_template("home.html", error="Error occurred while processing the request")
    return render_template("home.html")

if __name__ == "__main__":
    app.run(port=8000)