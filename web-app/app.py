'''
Web applicaiton for our machine learning client that takes in text and corrects the errors.
'''

from flask import Flask, request, jsonify, render_template
from machineClient.grammar_check import check_grammar
from machineClient.db import store_results
# pylint: disable=import-error

app = Flask(__name__)

'''
home page of the web app
'''
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        passage = request.form['userInput']
        original_passage, fixed_passage, error_analysis, api_response = check_grammar(passage)
        store_results(original_passage, fixed_passage, error_analysis, api_response)
        return render_template(
            'home.html',
            passage=original_passage,
            fixed_passage=fixed_passage,
            error_analysis=error_analysis
        )
    return render_template('home.html')

'''
call to analyze the user inputed text with grammar checker
'''
@app.route("/analyze", methods=["POST"])
def analyze_passage():
    try:
        passage = request.json["passage"]
    except KeyError:
        return jsonify({"error": "Missing 'passage' key in the request payload"}), 400

    original_passage, fixed_passage, error_analysis, api_response = check_grammar(passage)
    store_results(original_passage, fixed_passage, error_analysis, api_response)
    return jsonify({"fixed_passage": fixed_passage, "error_analysis": error_analysis})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
