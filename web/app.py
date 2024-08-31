import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from flask import Flask, render_template, request, jsonify
from chatbot import QAChatbot

app = Flask(__name__)
chatbot = QAChatbot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json['question']
    urls = request.json.get('urls', ["https://haystack.deepset.ai/blog/introducing-haystack-2-beta-and-advent"])
    answers = chatbot.ask_question(question, urls)
    return jsonify({'answers': answers})

if __name__ == '__main__':
    app.run(debug=True)