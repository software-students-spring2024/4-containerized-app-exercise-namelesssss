from flask import Flask, request, jsonify
from grammar_check import check_grammar
from db import store_results

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze_passage():
    try:
        passage = request.json["passage"]
    except KeyError:
        return jsonify({"error": "Missing 'passage' key in the request payload"}), 400

    original_passage, fixed_passage, error_analysis = check_grammar(passage)
    store_results(original_passage, fixed_passage, error_analysis)
    return jsonify({"fixed_passage": fixed_passage, "error_analysis": error_analysis})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)