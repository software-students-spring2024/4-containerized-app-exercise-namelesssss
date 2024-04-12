from flask import Flask, request
import logging
import openai
import requests

MLClient = Flask(__name__)

@MLClient.route('/receive_passage', methods=['POST'])
def receive_passage():
    passage = request.form['passage']
    return "Received passage: " + passage

if __name__ == '__main__':
    MLClient.run(host="0.0.0.0", port=5002, debug=True)