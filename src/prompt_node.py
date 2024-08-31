from haystack.nodes import EmbeddingRetriever, PromptNode, PromptTemplate
from transformers import pipeline as hf_pipeline

def get_prompt_node():
    model_name = "google/flan-t5-large"
    hf_pipeline = hf_pipeline("text2text-generation", model=model_name, device=0)  # Use GPU

    PromptTemplate(
        name="question-answering",
        prompt_text="""Answer the question based on the given context. If you cannot find an answer in the context, say "I don't know."

Context: {join(documents)}

Question: {query}

Answer:"""
    )

    return PromptNode(model_name_or_path=model_name, default_prompt_template="question-answering", use_gpu=False)