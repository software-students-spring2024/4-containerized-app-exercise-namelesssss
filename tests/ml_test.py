from machine-learning-client.grammar_check import check_grammar, extract_data, analyze_errors
from machine-learning-client.db import store_results

def test_check_grammar():
    passage = "This is a test passage with some grammer errors. It have a few spelling mistake and verb tense isues."
    original_passage, corrected_text, error_analysis, api_response = check_grammar(passage)

    assert original_passage == passage
    assert corrected_text == "This is a test passage with some grammar errors. It has a few spelling mistakes and verb tense issues."
    assert error_analysis == {
        "spelling": 2,
        "verb/tense": 2,
        "article/preposition": 0,
        "other": 0,
    }
    print("check_grammar test passed!")

def test_extract_data():
    output = "Corrected text: This is a test passage.\nError summary: spelling: [0]; verb/tense: [0]; article/preposition: [0]; other: [0]"
    corrected_text, error_summary = extract_data(output)

    assert corrected_text == "This is a test passage."
    assert error_summary == "Error summary: spelling: [0]; verb/tense: [0]; article/preposition: [0]; other: [0]"
    print("extract_data test passed!")

def test_analyze_errors():
    error_summary = "Error summary: spelling: [2]; verb/tense: [1]; article/preposition: [0]; other: [1]"
    error_analysis = analyze_errors(error_summary)

    assert error_analysis == {
        "spelling": 2,
        "verb/tense": 1,
        "article/preposition": 0,
        "other": 1,
    }
    print("analyze_errors test passed!")

def test_store_results():
    original_passage = "This is a test passage."
    corrected_text = "This is a test passage."
    error_analysis = {
        "spelling": 0,
        "verb/tense": 0,
        "article/preposition": 0,
        "other": 0,
    }
    api_response = "Corrected text: This is a test passage.\nError summary: spelling: [0]; verb/tense: [0]; article/preposition: [0]; other: [0]"

    store_results(original_passage, corrected_text, error_analysis, api_response)
    print("store_results test passed!")

def test_grammar_check_integration():
    passage = "This is a test passage with some grammer errors. It have a few spelling mistake and verb tense isues."
    original_passage, corrected_text, error_analysis, api_response = check_grammar(passage)

    assert original_passage == passage
    assert corrected_text == "This is a test passage with some grammar errors. It has a few spelling mistakes and verb tense issues."
    assert error_analysis == {
        "spelling": 2,
        "verb/tense": 2,
        "article/preposition": 0,
        "other": 0,
    }

    store_results(original_passage, corrected_text, error_analysis, api_response)
    print("Grammar check integration test passed!")

if __name__ == "__main__":
    test_check_grammar()
    test_extract_data()
    test_analyze_errors()
    test_store_results()
    test_grammar_check_integration()