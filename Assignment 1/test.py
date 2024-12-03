import os
import tkinter as tk
from tkinter import font

# Node class for our linked list-based dictionary
class Node:
    def __init__(self, key, value):
        self.key = key # Filename
        self.value = value # List of nouns
        self.next = None # Pointer to next node

# Custom linked-list based dictionary
class LinkedListDict:
    def __init__(self):
        self.head = None # Head node of linked list

    def insert(self, key, value): # Insert a new key-value pair
        node = self.head # Start at the head node
        while node: # Traverse the linked list
            if node.key == key: # If key already exists, update the value
                node.value = value # Update value and
                return # Return early
            node = node.next # Move to the next node
        
        new_node = Node(key, value)    # Create a new node
        new_node.next = self.head     # Point new node to the current head
        self.head = new_node         # Update head to the new node

    def get(self, key): # Retrieve value by key
        node = self.head # Start at the head node
        while node:     # Traverse the linked list
            if node.key == key: # If key matches, return the value
                return node.value   # Return the value
            node = node.next # Move to the next node
        return None

    def search_content(self, word):
        matching_documents = []
        node = self.head
        while node:
            if word in node.value:
                matching_documents.append(node.key)
            node = node.next
        return matching_documents

# Preprocess text by removing non-alphanumeric characters and splitting into words
def preprocess(text):
    text = ''.join(c.lower() if c.isalnum() or c.isspace() else ' ' for c in text)
    return text.split()

# Checks for the noun that ends with ing or ed or ly
def is_noun(word): 
    if word.endswith(('ing', 'ed', 'ly')):
        return False
    
    # Common non-nouns to exclude
    common_non_nouns = {
        "the", "and", "a", "an", "in", "on", "at", "with", "for", "from", "to", "by",
        "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "do", 
        "does", "did", "will", "would", "can", "could", "shall", "should", "may", 
        "might", "must", "who", "what", "where", "when", "why", "how", "like", "unlike", 
        "often", "more", "over", "under", "between", "through", "against", "around", 
        "throughout", "upon", "among", "within", "along", "even", "though", "although", 
        "however", "unless", "until", "while", "whilst", "whereas", "whether", "if", "unless",
        "because", "since", "so", "therefore", "thus", "hence", "accordingly", "consequently",
        "as", "like", "such", "including", "known", "chosen", "time", "times", "year", "years", 
        "day", "days", "week", "weeks", "month", "months", "hour", "hours","there"
    }

    if word in common_non_nouns:
        return False
    
    if word.istitle():
        return True
    
    common_noun_suffixes = ('ness', 'ity', 'tion', 'ment', 'ship', 'hood', 'dom', 'er', 'or')
    if word.endswith(common_noun_suffixes):
        return True
    
    if word.endswith(('s', 'es')):
        return True

    return False

def extract_nouns(text):
    words = preprocess(text)
    nouns = [word for word in words if is_noun(word)]
    return nouns

def process_documents(directory="./documents"):
    index = LinkedListDict()

    if not os.path.exists(directory):
        # print(f"Directory '{directory}' does not exist.")
        return index

    # Loading the documents
    for filename in os.listdir(directory): # Iterate over files in the directory
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            try:
                with open(file_path, "r") as file:
                    content = file.read()
                    nouns = extract_nouns(content)
                    # print(f"Inserting document '{filename}' with nouns: {nouns}")  # Debug: Print each document name and nouns
                    index.insert(filename, nouns)
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")

    return index




# Tkinter GUI
class DocumentSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Document Search App")
        self.root.geometry("600x550")
        self.root.config(bg="#f5f5f5")

        self.index = process_documents("./documents")
        
        # Fonts and styling
        header_font = font.Font(family="Helvetica", size=14, weight="bold")
        button_font = font.Font(family="Helvetica", size=10, weight="bold")

        # Directory label
        self.directory_label = tk.Label(root, text="Directory: ./documents", font=header_font, bg="#f5f5f5", fg="#333")
        self.directory_label.pack(pady=(20, 10))

        # Title search
        self.title_label = tk.Label(root, text="Search by Title:", bg="#f5f5f5", fg="#333")
        self.title_label.pack(pady=(10, 0))
        self.title_entry = tk.Entry(root, width=40)
        self.title_entry.pack(pady=(0, 5))
        self.title_search_button = tk.Button(root, text="Search Title", command=self.search_by_title, font=button_font, bg="#4CAF50", fg="white", width=20)
        self.title_search_button.pack(pady=(0, 15))

        # Content search
        self.content_label = tk.Label(root, text="Search by Content:", bg="#f5f5f5", fg="#333")
        self.content_label.pack(pady=(10, 0))
        self.content_entry = tk.Entry(root, width=40)
        self.content_entry.pack(pady=(0, 5))
        self.content_search_button = tk.Button(root, text="Search Content", command=self.search_by_content, font=button_font, bg="#2196F3", fg="white", width=20)
        self.content_search_button.pack(pady=(0, 15))

        # Show all button
        self.show_all_button = tk.Button(root, text="Show All Processed Documents", command=self.show_all_documents, font=button_font, bg="#FF9800", fg="white", width=25)
        self.show_all_button.pack(pady=(0, 20))

        # Results display
        self.results_text = tk.Text(root, wrap="word", height=12, width=65, bg="#e8e8e8", fg="#333")
        self.results_text.pack(pady=20)

    # Modify search_by_title to add debugging and ensure matching
    def search_by_title(self):
        title = self.title_entry.get().strip()
        # Attempt to retrieve with both title and title + .txt
        nouns = self.index.get(title) or self.index.get(f"{title}.txt")
        self.results_text.delete("1.0", tk.END)
        if nouns:
            self.results_text.insert(tk.END, f"Document with title '{title}' found.")
        else:
            print(f"Document titled '{title}' not found in index.")  # Debug: Print when document not found
            self.results_text.insert(tk.END, f"Document titled '{title}' not found.")

    def search_by_content(self):
        word = self.content_entry.get().strip().lower()
        matching_docs = self.index.search_content(word)
        self.results_text.delete("1.0", tk.END)
        if matching_docs:
            self.results_text.insert(tk.END, f"Documents containing the word '{word}': {matching_docs}")
        else:
            self.results_text.insert(tk.END, f"No documents found containing the word '{word}'.")

    def show_all_documents(self):
        # Display all processed documents and their nouns
        self.results_text.delete("1.0", tk.END)
        current = self.index.head
        if current is None:
            self.results_text.insert(tk.END, "No documents found in './documents' directory.")
            return
        while current:
            self.results_text.insert(tk.END, f"Document: {current.key}\nNouns: {current.value}\n\n")
            current = current.next

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = DocumentSearchApp(root)
    root.mainloop()
