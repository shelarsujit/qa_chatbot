from haystack.document_stores import ElasticsearchDocumentStore

def get_document_store():
    return ElasticsearchDocumentStore(
        host="localhost",
        username="",
        password="",
        index="document"
    )