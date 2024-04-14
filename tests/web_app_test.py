# Web App Tests
# Coveage Progress: 0%
import pytest

# Web app tests!!

# ** STRUCUTRE **
# def test_namey_name():
#   do something
#   more something
# assert THING == THING2
# repeat assert things until every part of that portion is tested

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