from flask import Flask, request, jsonify, render_template
from grammar_check import check_grammar
from db import store_results

app = Flask(__name__, template_folder='../web-app/templates')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        passage = request.form['passage']
        original_passage, fixed_passage, error_analysis, api_response = check_grammar(passage)
        store_results(original_passage, fixed_passage, error_analysis, api_response)
        return render_template('home.html', passage=original_passage, fixed_passage=fixed_passage, error_analysis=error_analysis)
    return render_template('home.html')

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
    app.run(host="0.0.0.0", port=5050)