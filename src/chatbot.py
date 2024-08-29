import os
from pypdf import PdfReader
from docx import Document
from pptx import Presentation
from bs4 import BeautifulSoup
from haystack.pipelines import Pipeline
from haystack.utils import print_answers
from .document_store import get_document_store
from .retriever import get_retriever
from .prompt_node import get_prompt_node

class QAChatbot:
    def __init__(self):
        self.document_store = get_document_store()
        self.retriever = get_retriever(self.document_store)
        self.prompt_node = get_prompt_node()
        self.pipe = self._create_pipeline()

    def _create_pipeline(self):
        pipe = Pipeline()
        pipe.add_node(component=self.retriever, name="Retriever", inputs=["Query"])
        pipe.add_node(component=self.prompt_node, name="PromptNode", inputs=["Retriever"])
        return pipe

    def add_documents(self, docs):
        self.document_store.write_documents(docs)
        self.document_store.update_embeddings(self.retriever)

    def ask_question(self, question):
        result = self.pipe.run(query=question, params={"Retriever": {"top_k": 3}})
        print_answers(result, details="minimum")

    def ingest_pdf(self, file_path):
        docs = []
        pdf_reader = PdfReader(file_path)
        for page in pdf_reader.pages:
            text = page.extract_text()
            if text.strip():
                docs.append({"content": text, "meta": {"filename": os.path.basename(file_path)}})
        return docs

    def ingest_docx(self, file_path):
        docs = []
        doc = Document(file_path)
        for para in doc.paragraphs:
            if para.text.strip():
                docs.append({"content": para.text, "meta": {"filename": os.path.basename(file_path)}})
        return docs

    def ingest_pptx(self, file_path):
        docs = []
        prs = Presentation(file_path)
        for slide in prs.slides:
            slide_text = []
            for shape in slide.shapes:
                if hasattr(shape, 'text'):
                    slide_text.append(shape.text)
            if slide_text:
                docs.append({"content": "\n".join(slide_text), "meta": {"filename": os.path.basename(file_path)}})
        return docs

    def ingest_html(self, file_path):
        docs = []
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'lxml')
            text = soup.get_text(separator='\n', strip=True)
            docs.append({"content": text, "meta": {"filename": os.path.basename(file_path)}})
        return docs

    def ingest_documents(self, directory):
        docs = []
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if filename.endswith('.pdf'):
                docs.extend(self.ingest_pdf(file_path))
            elif filename.endswith('.docx'):
                docs.extend(self.ingest_docx(file_path))
            elif filename.endswith('.pptx'):
                docs.extend(self.ingest_pptx(file_path))
            elif filename.endswith('.html'):
                docs.extend(self.ingest_html(file_path))
        
        if docs:
            self.add_documents(docs)
            print(f"Ingested {len(docs)} documents from {len(os.listdir(directory))} files.")
        else:
            print("No valid documents found in the specified directory.")

def main():
    chatbot = QAChatbot()
    
    # Ingest documents from a directory
    document_directory = "D:\Sujit\documents"  # Replace with the actual path to your document files
    chatbot.ingest_documents(document_directory)

    print("Welcome to the Q&A Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        chatbot.ask_question(user_input)

if __name__ == "__main__":
    main()