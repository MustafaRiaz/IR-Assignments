import os

DOCUMENTS_DIR = './documents'
def list_documents():
    return [doc for doc in os.listdir(DOCUMENTS_DIR) if doc.endswith('.txt')]

def search_by_title(title):
    documents = list_documents()
    for doc in documents:
        if title.lower() in doc.lower():
            print(f"Document found: {doc}")
            return os.path.join(DOCUMENTS_DIR, doc)
    print("Document not found.")
    return None

def display_document(file_path):
    if file_path:
        with open(file_path, 'r') as file:
            print(file.read())

search_title = input("Enter the document title to search: ")
file_path = search_by_title(search_title)
display_document(file_path)
