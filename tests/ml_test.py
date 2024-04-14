# Machine Learning Tests
# Coveage Progress: 0%
import pytest
from db import store_results
from grammar_check import check_grammar, extract_data, analyze_errors

# Machine learning tests!!

# ** STRUCUTRE **
# def test_namey_name():
#   do something
#   more something
# assert THING == THING2
# repeat assert things until every part of that portion is tested


# db.py tests:

def test_db_storage():
    # def store results
    # adds results to the database
    # stores: original_passage, fixed_passage, error_analysis, api_response)
    # i think i wanna make sure it stores correctly by checking each individually ??? idk

    # store_results(original_passage, fixed_passage, error_analysis, api_response)
    # it might be better to just run it so i can get the api_response that way
    original_passage = "I like pengiuns."
    fixed_passage = "I like pengiuns."
    error_analysis = {
        "spelling": 1,
        "verb/tense": 0,
        "article/preposition": 0,
        "other": 0
    }
    # api_response = 
    # WHAT IS THE API RESPONSE

def test_db_running():
    # if needed for coverage, could test to see if db is running properly
    passage = "There is no passage here"



# grammar.py tests:


def test_check_grammar():
    # def check_grammar(passage)
    # return passage, corrected_text, error_analysis, output
    passage = "I am perfect."


def test_extract_data():
    passage = "uhhh"
    # def extract_data
    # return corrected_text, error_summary

def test_analyze_error():
    passage = "uhhh"
    # def analyze_errors
    # return error_analysis