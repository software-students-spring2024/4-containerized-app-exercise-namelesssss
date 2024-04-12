from flask import Flask, request, jsonify, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    if request.method == 'POST':
        passage = request.form['userInput']
        response = requests.post("http://back-end:5002", data={'passage':passage})
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

'''
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        passage = request.form['passage']
        original_passage, fixed_passage, error_analysis = check_grammar(passage)
        return render_template('home.html', fixed_passage=fixed_passage, error_analysis=error_analysis)
    return render_template('home.html')
'''