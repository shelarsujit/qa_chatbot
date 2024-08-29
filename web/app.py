from flask import Flask, render_template, request, jsonify
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from chatbot import QAChatbot

app = Flask(__name__)
chatbot = QAChatbot()

# Ingest documents when the app starts
document_directory = "D:\Sujit\documents"  # Replace with the actual path
chatbot.ingest_documents(document_directory)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json['question']
    answer = chatbot.ask_question(question)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)