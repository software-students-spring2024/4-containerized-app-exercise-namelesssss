"""
Web applicaiton for our machine learning client that takes in text and corrects the errors.
"""

# pylint: disable=import-error
# pylint: disable=missing-function-docstring
from flask import Flask, request, jsonify, render_template
from machineClient.grammar_check import check_grammar
from machineClient.db import store_results

app = Flask(__name__)

"""
home page of the web app
"""


@app.route("/", methods=["GET", "POST"])
def home():
    "Home page of the web app."
    if request.method == "POST":
        passage = request.form["passage"]
        original_passage, fixed_passage, error_analysis, api_response = check_grammar(
            passage
        )
        store_results(original_passage, fixed_passage, error_analysis, api_response)
        return render_template(
            "home.html",
            passage=original_passage,
            fixed_passage=fixed_passage,
            error_analysis=error_analysis,
        )
    return render_template("home.html")


@app.route("/analyze", methods=["POST"])
def analyze_passage():
    """Analyze the provided passage"""
    if 'passage' not in request.json:
        return jsonify({"Error: "Missing 'passage' key in the request payload"}), 400
    passage = request.json["passage"]
    original_passage, fixed_passage, error_analysis, api_response=check_grammar(passage)
    store_results(original_passage, fixed_passage, error_analysis, api_response)
    return jsonify({"fixed_passage": fixed_passage, "error_analysis": error_analysis})
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
