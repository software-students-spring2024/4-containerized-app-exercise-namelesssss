# Nameless Grammar Checker

[![web-app lint-free](https://github.com/software-students-spring2024/4-containerized-app-exercise-namelesssss/actions/workflows/lint.yml/badge.svg)](https://github.com/software-students-spring2024/4-containerized-app-exercise-namelesssss/actions/workflows/lint.yml)
[![machine-learning-client lint-free](https://github.com/software-students-spring2024/4-containerized-app-exercise-namelesssss/actions/workflows/lint.yml/badge.svg)](https://github.com/software-students-spring2024/4-containerized-app-exercise-namelesssss/actions/workflows/lint.yml)

## Description

Nameless Grammar Checker is a simple grammar checker that takes user-inputted text and parses the information with OpenAI's grammar checking API. It outputs a corrected version of the inputted passage along with the number of grammatical errors it detected.

## Instructions

### API Key
- Go to your OpenAI account and navigate to "[View API Keys](https://platform.openai.com/account/api-keys)"
- Select "Create new secret key"
- Copy the key and insert it into your file `Dockerfile-web-app` (replace `OPENAI API KEY HERE` with your API Key). Alternatively, use `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` if you do not have one.
```
ENV OPENAI_API_KEY= OPENAI API KEY HERE
```
- Save the changes

### Run the grammar checker with Docker
- Now, open up your terminal and navigate to the root folder
- Run the command `docker-compose up`

### Access the web app
- Open up your web browser and enter `localhost:5001`

## Contributors
* [Hannah Horiuchi](https://github.com/hah8236)
* [Jiahua Liao](https://github.com/Jiahuita)
* [Kevin Lin](https://github.com/Kalados)
* [Nicole Luzuriaga](https://github.com/nicjluz)

