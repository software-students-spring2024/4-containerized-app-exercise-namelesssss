FROM python:3.12-slim

WORKDIR /machine-learning-client

COPY . /machine-learning-client
RUN pip3 install -r requirements.txt

EXPOSE 5002

CMD [ "python3", "grammar_check.py"]