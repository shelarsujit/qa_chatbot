from haystack.nodes import EmbeddingRetriever

def get_retriever(document_store):
    return EmbeddingRetriever(
        document_store=document_store,
        embedding_model="sentence-transformers/multi-qa-mpnet-base-dot-v1",
        use_gpu=False
    )