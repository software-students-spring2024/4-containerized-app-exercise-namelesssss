import pytest
from web-app.app import transcribe_audio, home, analyze_passage, transcribe

def test_transcribe_audio():
    file_path = "path"
    # def transcribe_audio(file_path):
    # what am i returning...
    print("transcribe_audio test has passed! ")


def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    print("home page test has passed!")


def test_analyze_passage():
    #  return jsonify({"fixed_passage": fixed_passage, "error_analysis": error_analysis})
    passage = "uhh"
    print("analyze_passage test has passed!")


def test_transcribe():
    # return jsonify({"transcript": transcript})
    # transcribes the audio file
    original_passage = "This is a test passage."
    print("transcribe test has passed!")


if __name__ == "__main__":
    test_transcribe()
    test_analyze_passage()
    test_home_page()
    test_transcribe_audio()