import pytest
from src.chatbot import QAChatbot

@pytest.fixture
def chatbot():
    return QAChatbot()

def test_chatbot_initialization(chatbot):
    assert chatbot.document_store is not None
    assert chatbot.retriever is not None
    assert chatbot.prompt_node is not None
    assert chatbot.pipe is not None

def test_add_documents(chatbot):
    docs = [
        {"content": "Test document 1"},
        {"content": "Test document 2"}
    ]
    chatbot.add_documents(docs)
    # You might need to implement a method to check the document count
    # assert chatbot.document_store.get_document_count() == 2

def test_ask_question(chatbot, capsys):
    chatbot.add_documents([{"content": "The capital of France is Paris."}])
    chatbot.ask_question("What is the capital of France?")
    captured = capsys.readouterr()
    assert "Paris" in captured.out