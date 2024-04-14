# pylint: disable=import-error
import os
import deepspeech
import numpy as np
from flask import Flask, request, jsonify, render_template
from machineClient.grammar_check import check_grammar
from machineClient.db import store_results

app = Flask(__name__)

def transcribe_audio(audio_file):
    """
    Transcribe the provided audio file using DeepSpeech
    """
    model_file_path = 'deepspeech-0.9.3-models.pbmm'
    model = deepspeech.Model(model_file_path)
    buffer = np.frombuffer(audio_file.read(), dtype=np.int16)
    transcript = model.stt(buffer)
    return transcript.strip()

@app.route("/", methods=["GET", "POST"])
def home():
    """
    Home page of the web app.
    """
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
    """
    Analyze the provided passage
    """
    if "passage" not in request.json:
        return jsonify({"Error": "Missing 'passage' key in the request payload"}), 400
    passage = request.json["passage"]
    original_passage, fixed_passage, error_analysis, api_response = check_grammar(
        passage
    )
    store_results(original_passage, fixed_passage, error_analysis, api_response)
    return jsonify({"fixed_passage": fixed_passage, "error_analysis": error_analysis})

@app.route("/transcribe", methods=["POST"])
def transcribe():
    """
    Transcribe the provided audio file
    """
    if "audio_file" not in request.files:
        return (
            jsonify({"Error": "Missing 'audio_file' key in the request payload"}),
            400,
        )
    audio_file = request.files["audio_file"]
    if audio_file.filename == '':
        return jsonify({"Error": "No selected file"}), 400
    if audio_file and allowed_file(audio_file.filename):
        transcript = transcribe_audio(audio_file)
        return jsonify({"transcript": transcript})
    return jsonify({"Error": "Invalid file type"}), 400

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'wav', 'mp3', 'ogg'}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
