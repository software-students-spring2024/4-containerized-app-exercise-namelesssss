'''
grammar checking file for our machine-learning-client
'''

import logging
import openai
from app_config import OPENAI_API_KEY
# pylint: disable=line-too-long
# pylint: disable=no-member

openai.api_key = OPENAI_API_KEY

logger = logging.getLogger(__name__)

'''
Grammar checker from openAI
'''
def check_grammar(passage):
    try:
        prompt = (
            f"Check the grammar of the text and provide the number of grammar errors sorted by type, "
            f"along with a corrected version of the text. strictly follow the following format "
            f"for the result output with no additional outputs: corrected text: "
            f"[text]\n error summary: [spelling:[number]];[verb/tense:[number]];"
            f"[article/preposition:[number]];[other:[number]]\n\nText: {passage}"
        )
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "user",
                    "content": "Check the grammar of the provided text and provide the number of grammar "
                               "errors sorted by type, along with a corrected version of the text. "
                               "strictly follow the following format for the result output with no "
                               "additional outputs: corrected text: [text]\n error summary: "
                               "[spelling:[number]];[verb/tense:[number]];[article/preposition:[number]];"
                               "[other:[number]]\\n\\nText: {\"I drank juice.\"}"
                },
                {
                    "role": "assistant",
                    "content": "Corrected text: I drink juice.\n Error summary: spelling:[0]; verb/tense:[1]; "
                               "article/preposition:[0]; other:[0]"
                },
                {
                    "role": "user",
                    "content": "Check the grammar of the provided text and provide the number of grammar errors sorted "
                               "by type, along with a corrected version of the text. strictly follow the following "
                               "format for the result output with no additional outputs: corrected text: "
                               "[text]\n error summary: [spelling:[number]];[verb/tense:[number]];"
                               "[article/preposition:[number]];[other:[number]]\\n\\nText: {\"I wants peer juice.\"}"
                },
                {
                    "role": "assistant",
                    "content": "Corrected text: I want pear juice.\n Error summary: spelling:[1]; verb/tense:[1]; "
                               "article/preposition:[0]; other:[0]"
                },
                {
                    "role": "user", "content": prompt
                }
            ],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        output = response.choices[0].message['content'].strip()
        corrected_text, error_summary = extract_data(output)
        error_analysis = analyze_errors(error_summary)
        return passage, corrected_text, error_analysis, output
    except openai.error.APIError as e:
        logger.error(f"OpenAI API error: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        raise

def extract_data(output):
    corrected_text = ""
    error_summary = ""
    lines = output.split("\n")
    for line in lines:
        if line.lower().startswith("corrected text:"):
            corrected_text = line.split(":", 1)[1].strip()
        elif line.lower().startswith("error summary:"):
            error_summary = line.split(":", 1)[1].strip()
    return corrected_text, error_summary

def analyze_errors(error_summary):
    error_analysis = {
        "spelling": 0,
        "verb/tense": 0,
        "article/preposition": 0,
        "other": 0
    }

    error_types = ["spelling", "verb/tense", "article/preposition", "other"]

    for error_type in error_types:
        try:
            count = int(error_summary.split(f"{error_type}:[")[1].split("]")[0])
            error_analysis[error_type] = count
        except (IndexError, ValueError):
            error_analysis[error_type] = 0

    return error_analysis
