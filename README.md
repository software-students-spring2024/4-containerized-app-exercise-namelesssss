# Nameless Grammar Checker

[![web-app lint-free](https://github.com/software-students-spring2024/4-containerized-app-exercise-namelesssss/actions/workflows/lint.yml/badge.svg)](https://github.com/software-students-spring2024/4-containerized-app-exercise-namelesssss/actions/workflows/lint.yml)
[![machine-learning-client lint-free](https://github.com/software-students-spring2024/4-containerized-app-exercise-namelesssss/actions/workflows/lint.yml/badge.svg)](https://github.com/software-students-spring2024/4-containerized-app-exercise-namelesssss/actions/workflows/lint.yml)

## Description

Nameless Grammar Checker is a web-based grammar checking application that utilizes OpenAI's language model to analyze and correct user-inputted text. The application provides a user-friendly interface where users can input their text, and the system will generate a corrected version of the passage along with a summary of the grammatical errors detected.

## Architecture

The Nameless Grammar Checker consists of two main components:

1. **Web Application**: The web application is built using a web framework (e.g., Flask, Django) and provides the user interface for inputting text and displaying the grammar checking results. It communicates with the machine learning client to process the user's input and retrieve the corrected text and error analysis.

2. **Machine Learning Client**: The machine learning client is responsible for interacting with the OpenAI API to perform grammar checking. It takes the user's input, sends it to the OpenAI API for processing, and retrieves the corrected text and error analysis. The client is implemented in Python and utilizes the OpenAI library for API communication.

## Key Files

- `app_config.py`: Contains configuration settings for the application, including the OpenAI API key and MongoDB URI.
- `db.py`: Handles the database connection and provides functions for storing grammar checking results in MongoDB.
- `grammar_check.py`: Implements the core grammar checking functionality, including sending requests to the OpenAI API, extracting the corrected text and error summary, and analyzing the error counts.
- `ml_test.py`: Contains unit tests for the machine learning client, ensuring the correctness of the grammar checking functionality.
- [To be added]

## Instructions

### API Key Setup

1. Obtain an OpenAI API key by following these steps:
   - Go to your OpenAI account and navigate to "[View API Keys](https://platform.openai.com/account/api-keys)".
   - Select "Create new secret key".
   - Copy the generated API key.
2. Insert the API key into the `Dockerfile-web-app` file:
   - Replace `OPENAI API KEY HERE` with your API key.
   - Save the changes.

   Alternatively, you can use [this shared API key](https://docs.google.com/document/d/1EczE__RJvVKTikYvHHtuQ-0u92QCvKg3TYBN5e4fWgk/edit?usp=sharing) if you don't have your own (requires an NYU email).

### Running the Application with Docker

1. Open a terminal and navigate to the root folder of the project.
2. Run the command `docker-compose up --build` to build and start the application containers.

### Accessing the Web Application

1. Open a web browser and visit `localhost:5001` to access the Nameless Grammar Checker web application.
2. Enter the text you want to check for grammar errors in the provided input field.
3. Click the "Check Grammar" button to submit the text for analysis.
4. The application will display the corrected version of the text along with a summary of the grammatical errors detected.

## Testing

The project includes unit tests for the machine learning client to ensure the correctness of the grammar checking functionality. To run the tests, follow these steps:

1. Navigate to the `tests` directory.
2. Run the command `python ml_test.py` and `python web_app_test.py` to execute the test suite.
3. The test results will be displayed in the console, indicating whether the tests passed or failed.

## Contributors

- [Hannah Horiuchi](https://github.com/hah8236)
- [Jiahua Liao](https://github.com/Jiahuita)
- [Kevin Lin](https://github.com/Kalados)
- [Nicole Luzuriaga](https://github.com/nicjluz)