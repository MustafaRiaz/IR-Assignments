import os

# Step 1: Define the Node class for Linked List
class Node:
    def __init__(self, data=None):
        self.data = data  # Data to store (word or document name)
        self.next = None  # Pointer to the next node

# Step 2: Define the LinkedList class to manage nodes
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        """Insert new data (word or document name) at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def search(self, data):
        """Search for data in the linked list and return True if found."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def display(self):
        """Display all elements in the linked list."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Step 3: Create an Index using LinkedList
class DocumentIndex:
    def __init__(self):
        self.index = {}  # Index of words pointing to linked lists of documents
    
    def add_word(self, word, document):
        """Add word to the index with a reference to the document."""
        if word not in self.index:
            self.index[word] = LinkedList()
        if not self.index[word].search(document):  # Avoid duplicate document entries
            self.index[word].insert(document)
    
    def search_word(self, word):
        """Search for a word in the index and return the list of documents."""
        if word in self.index:
            return self.index[word].display()
        return []

# Step 4: Preprocess the text (Remove punctuation and convert to lowercase)
def preprocess_text(text):
    """Custom function to remove non-alphabetic characters and convert to lowercase."""
    clean_text = ''.join([char.lower() if char.isalnum() else ' ' for char in text])
    return clean_text

# Step 5: Read and Index Documents using LinkedList
def index_documents(doc_index, folder):
    """Read all documents in the folder and index words."""
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            with open(os.path.join(folder, filename), 'r', encoding='utf-8') as file:
                content = file.read()
                content = preprocess_text(content)
                words = content.split()
                for word in words:
                    doc_index.add_word(word, filename)

# Step 6: Build a Search Function
def search_documents(doc_index, query):
    """Search for a word in the index."""
    query = preprocess_text(query)
    return doc_index.search_word(query)

# Step 7: Display Results
def display_results(results):
    """Display search results."""
    if results:
        print(f"Found in documents: {', '.join(results)}")
    else:
        print("No matching documents found.")

# Main Function
def main():
    # Initialize the document index
    doc_index = DocumentIndex()

    # Index the documents in the specified folder
    print("Indexing documents...")
    index_documents(doc_index, "documents")  # Assuming 'documents' folder contains text files
    print("Indexing complete!")

    # Main search loop
    while True:
        query = input("Enter a word to search (or 'exit' to quit): ")
        if query == 'exit':
            break
        results = search_documents(doc_index, query)
        display_results(results)

if __name__ == "__main__":
    main()
 