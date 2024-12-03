import os
from colorama import Fore, Style, init
import re

# Initialize colorama
init(autoreset=True)

# Step 1: Define the Node class for Linked List
class Node:
    def __init__(self, data=None):
        self.data = data  # Data to store (document name)
        self.next = None  # Pointer to the next node

# Step 2: Define the LinkedList class to manage nodes
class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0  # Track how many documents contain the word
    
    def insert(self, data):
        """Insert new data (document name) if it's not already in the list."""
        if not self.search(data):  # Avoid duplicates
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node
            self.count += 1  # Increment the document count
    
    def search(self, data):
        # Search for data in the linked list and return True if found.
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def display_documents(self):
        """Display all documents in the linked list."""
        documents = []
        current = self.head
        while current:
            documents.append(current.data)
            current = current.next
        return documents
    
    def get_document_count(self):
        """Return the count of unique documents containing the word."""
        return self.count

# Step 3: Create an Index using LinkedList and store document content
class DocumentIndex:
    def __init__(self):
        self.index = {}  # Dictionary to store words with linked lists of documents
        self.documents = {}  # Dictionary to store actual document content
    
    def add_document(self, document_name, content):
        """Store the document content and index words."""
        self.documents[document_name] = content
        words = set(preprocess_text(content).split())  # Index words without duplicates
        for word in words:
            self.add_word(word, document_name)
    
    def add_word(self, word, document):
        """Add word to the index, tracking its appearances across documents."""
        if word not in self.index:
            self.index[word] = LinkedList()
        self.index[word].insert(document)  # Add document only if not already listed
    
    def search_word(self, word):
        """Search for a word in the index and return document information."""
        if word in self.index:
            document_names = self.index[word].display_documents()
            return {
                'documents': document_names,
                'count': self.index[word].get_document_count(),
                'contents': {doc: self.documents[doc] for doc in document_names}
            }
        return {'documents': [], 'count': 0, 'contents': {}}

# Step 4: Enhanced Preprocessing (without external libraries)
def preprocess_text(text):
    """Preprocess text: remove punctuation, lowercase, remove stop words, and apply simple stemming."""
    # Define simple stopwords (a small set of common English words)
    stop_words = set([
        'a', 'an', 'the', 'and', 'but', 'or', 'so', 'for', 'nor', 'to', 'of', 'in', 'on', 'at', 'by', 'with', 'about', 'as', 'from', 'that', 'which', 'who', 'whom', 'this', 'it', 'its', 'i', 'you', 'he', 'she', 'we', 'they', 'them', 'their', 'ours', 'your', 'yours', 'is', 'are', 'was', 'were', 'be', 'been', 'being'
    ])
    
    # Simple stemming function: Remove common suffixes
    def simple_stem(word):
        if word.endswith('ing'):
            return word[:-3]
        elif word.endswith('ed'):
            return word[:-2]
        elif word.endswith('ly'):
            return word[:-2]
        return word
    
    # Remove non-alphabetic characters (punctuation) and tokenize
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Convert text to lowercase and split into words
    words = text.lower().split()
    
    # Remove stop words and apply stemming
    processed_words = [simple_stem(word) for word in words if word not in stop_words]
    
    return ' '.join(processed_words)

# Step 5: Load Documents and Store Content in Memory
def index_documents(doc_index, folder):
    """Read all documents in the folder and store content in memory."""
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            with open(os.path.join(folder, filename), 'r', encoding='utf-8') as file:
                content = file.read()
                doc_index.add_document(filename, content)

# Step 6: Build a Search Function
def search_documents(doc_index, query):
    """Search for a word in the index and retrieve document information and content."""
    query = preprocess_text(query)
    return doc_index.search_word(query)

# Step 7: Display Results
def display_results(results):
    """Display search results with document count and content."""
    print(Fore.CYAN + "-" * 40)
    if results['documents']:
        print(Fore.GREEN + f"Found in {results['count']} document(s):")
        for doc in results['documents']:
            print(Fore.YELLOW + f"\nDocument: {doc}")
            print(Fore.WHITE + f"Content: {results['contents'][doc]}")
    else:
        print(Fore.RED + "No matching documents found.")
    print(Fore.CYAN + "-" * 40)

# Console UI - Main Function
def main():
    # Header
    print(Fore.WHITE + Style.BRIGHT + "=" * 50)
    print(Fore.WHITE + Style.BRIGHT + "        Welcome to Document Search Indexer        ")
    print(Fore.WHITE + Style.BRIGHT + "=" * 50)
    
    # Initialize the document index
    doc_index = DocumentIndex()

    # Index the documents in the specified folder
    print(Fore.CYAN + "\nIndexing documents...")
    index_documents(doc_index, "documents")  # Assuming 'documents' folder contains text files
    print(Fore.GREEN + "Indexing complete!\n")

    # Main search loop
    while True:
        print(Fore.MAGENTA + Style.BRIGHT + "Enter a word to search (or 'exit' to quit):", end=" ")
        query = input().strip()
        
        if query.lower() == 'exit':
            print(Fore.CYAN + "Exiting the program. Goodbye!")
            break

        results = search_documents(doc_index, query)
        display_results(results)

if __name__ == "__main__":
    main()
