import openai
import logging

logger = logging.getLogger(__name__)

def check_grammar(passage):
    try:
        openai.api_key = "YOUR_API_KEY"
        prompt = f"Check the grammar of the text and provide the number of grammar errors sorted by type, along with a corrected version of the text. strictly follow the following format for the result output with no additional outputs: corrected text: [text] error summary: [spelling:[number]];[verb/tense:[number]];[article/preposition:[number]];[other:[number]]\n\nText: {passage}"
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7,
        )
        output = response.choices[0].text.strip()
        corrected_text, error_summary = parse_output(output)
        error_analysis = analyze_errors(error_summary)
        return passage, corrected_text, error_analysis
    except openai.error.AuthenticationError:
        logger.error("Invalid API key")
        raise
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        raise

def parse_output(output):
    corrected_text = ""
    error_summary = ""
    lines = output.split("\n")
    for line in lines:
        if line.startswith("corrected text:"):
            corrected_text = line.replace("corrected text:", "").strip()
        elif line.startswith("error summary:"):
            error_summary = line.replace("error summary:", "").strip()
    return corrected_text, error_summary

def analyze_errors(error_summary):
    error_analysis = {
        "spelling": 0,
        "verb/tense": 0,
        "article/preposition": 0,
        "other": 0
    }
    errors = error_summary.split(";")
    for error in errors:
        if ":" in error:
            try:
                error_type, count = error.split(":")
                error_analysis[error_type] = int(count)
            except (ValueError, KeyError):
                logger.warning(f"Unexpected error format: {error}")
    return error_analysis