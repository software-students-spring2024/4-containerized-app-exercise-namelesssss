"""
Web applicaiton for our machine learning client that takes in text and corrects the errors.
"""

# pylint: disable=import-error
# pylint: disable=missing-function-docstring
from flask import Flask, request, jsonify, render_template
from machineClient.grammar_check import check_grammar
from machineClient.db import store_results
<<<<<<< HEAD
from google.cloud import speech

=======
from google.cloud import speech_v1p1beta1 as speech
>>>>>>> 2d893df98db909ef669f652dc41840a8de3003fd
app = Flask(__name__)
"""
home page of the web app
"""
<<<<<<< HEAD


def transcribe_audio(file_path):
=======
def transcribe_audio(audio_file):
>>>>>>> 2d893df98db909ef669f652dc41840a8de3003fd
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
<<<<<<< HEAD
        return format(result.alternatives[0].transcript)


=======
        transcript += format(result.alternatives[0].transcript) + " "
    return transcript.strip()
>>>>>>> 2d893df98db909ef669f652dc41840a8de3003fd
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
    """Transcribe the provided audio file"""
    if "audio_file" not in request.files:
        return (
            jsonify({"Error": "Missing 'audio_file' key in the request payload"}),
            400,
        )
    audio_file = request.files["audio_file"]
    transcript = transcribe_audio(audio_file)
    return jsonify({"transcript": transcript})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
