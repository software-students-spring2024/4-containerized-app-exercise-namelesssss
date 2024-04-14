# Web App Tests
# Coveage Progress: 0%
import pytest
from web-app.app import transcribe_audio, home, analyze_passage, transcribe

# Web app tests!!

# ** STRUCUTRE **
# def test_namey_name():
#   do something
#   more something
# assert THING == THING2
# repeat assert things until every part of that portion is tested

# I want peer jiuce = I want pear juice
# Who am you = who are you\

def test_transcribe_audio():
    file_path = "path"
    # def transcribe_audio(file_path):
    # what am i returning...
    print("transcribe_audio test has passed! ")


def test_home_page():
    # testing the homepage
    # return render_template("home.html") 
    home = "uhhh"
    print("home page test has passed!")


def test_analyze_passage():
    #  return jsonify({"fixed_passage": fixed_passage, "error_analysis": error_analysis})
    passage = "uhh"
    print("analyze_passage test has passed!")


def test_transcribe():
    # return jsonify({"transcript": transcript})
    # transcribes the audio file
    audio_file = "uhh"
    print("transcribe test has passed!")

# might not need after all...
'''
def test_text_no_mistakes():
    passage = "I am perfect."
    expected_passage = "I am perfect."
    expected_error_analysis = {
        "spelling": 0,
        "verb/tense": 0,
        "article/preposition": 0,
        "other": 0
    }
    # assert expected_passage = [GETTING THE OUTCOME FOR THAT]
    # assert expected_error_analysis = [GETTING THE OUTCOME FOR THAT PT 2]


def test_text_mistakes():
    passage = "He be runnin."
    expected_passage = "He is running."
    # expected_error_analysis = 
    # assert expected_passage = [GETTING THE OUTCOME FOR THAT]
    # assert expected_error_analysis = [GETTING THE OUTCOME FOR THAT PT 2]


def test_voice_no_mistakes():
    # test a sound file too, not just via microphone
    expected_heard = "I am perfect."
    expected_passage = "I am perfect."
    # expected_error_analysis = 
    # assert expected_heard = the speech to text
    # assert expected_passage = [GETTING THE OUTCOME FOR THAT]
    # assert expected_error_analysis = [GETTING THE OUTCOME FOR THAT PT 2]


def test_voice_mistakes():
    # test a sound file too, not just via microphone
    expected_heard = "Who am you?"
    expected_passage = "Who are you?"
    # expected_error_analysis = 
    # assert expected_heard = the speech to text
    # assert expected_passage = [GETTING THE OUTCOME FOR THAT]
    # assert expected_error_analysis = [GETTING THE OUTCOME FOR THAT PT 2]

'''