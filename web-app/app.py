"""
Web applicaiton for our machine learning client that takes in text and corrects the errors.
"""

# pylint: disable=import-error
# pylint: disable=missing-function-docstring
# pylint: disable=missing-timeout
from io import BytesIO
from flask import Flask, request, jsonify, render_template
from machineClient.grammar_check import check_grammar
from machineClient.db import store_results
from google.cloud import speech
from google.api_core import exceptions
import requests

app = Flask(__name__)


def transcribe_audio(audio_file):
    try:
        client = speech.SpeechClient()
        content = audio_file.read()
        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code="en-US",
        )
        response = client.recognize(config=config, audio=audio)
        transcript = ""
        for result in response.results:
            transcript += format(result.alternatives[0].transcript) + " "
        return transcript.strip()
    except exceptions.InvalidArgument as e:
        app.logger.error("Error transcribing audio: %s", e)
        return None


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        passage = request.form["passage"]
        audio_file = request.files.get("audio_file")
        audio_data_url = request.form.get("audio_data")

        if audio_file:
            transcript = transcribe_audio(audio_file)
            if transcript:
                passage += " " + transcript
        elif audio_data_url:
            audio_data = requests.get(audio_data_url).content
            audio_file = BytesIO(audio_data)
            transcript = transcribe_audio(audio_file)
            if transcript:
                passage += " " + transcript

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
    input_passage = request.json.get("passage")
    if not input_passage:
        return jsonify({"Error": "Missing 'passage' key in the request payload"}), 400
    original_passage, fixed_passage, error_analysis, api_response = check_grammar(
        input_passage
    )
    store_results(original_passage, fixed_passage, error_analysis, api_response)
    return jsonify({"fixed_passage": fixed_passage, "error_analysis": error_analysis})


@app.route("/transcribe", methods=["POST"])
def transcribe():
    audio_file = request.files.get("audio_file")
    if not audio_file:
        return (
            jsonify({"Error": "Missing 'audio_file' key in the request payload"}),
            400,
        )
    transcript = transcribe_audio(audio_file)
    if not transcript:
        return jsonify({"Error": "Failed to transcribe audio"}), 500
    return jsonify({"transcript": transcript})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
