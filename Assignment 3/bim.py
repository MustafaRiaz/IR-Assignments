import os
import string
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QVBoxLayout, QWidget,
    QLabel, QLineEdit, QPushButton, QComboBox, QTextEdit, QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont

# Define your preprocessing and model functions here
STOPWORDS = {"and", "or", "the", "is", "in", "of", "to", "for", "a", "an", "on", "by", "at", "from", "with"}

SYNONYMS = {
    "nasa": ["space agency", "aerospace", "space organization"],
    "mars": ["planet", "martian"],
    "spacex": ["elon musk", "private space company"],
    "exploration": ["explore", "discovery", "research"]
}

def preprocess(text):
    tokens = text.lower().split()
    tokens = [token.strip(string.punctuation) for token in tokens]
    return [token for token in tokens if token and token not in STOPWORDS]

def load_documents(folder_path):
    documents = {}
    file_mapping = {}
    file_counter = 1
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                documents[file_counter] = preprocess(file.read())
                file_mapping[file_counter] = filename
                file_counter += 1
    return documents, file_mapping

def binary_independence_model(query, documents):
    query_terms = set(preprocess(query))
    term_matrix = {term: [0] * len(documents) for term in query_terms}
    
    for doc_id, tokens in documents.items():
        for term in query_terms:
            if term in tokens:
                term_matrix[term][doc_id - 1] = 1

    query_vector = [1 if term in query_terms else 0 for term in term_matrix]
    scores = []
    
    for doc_id in range(len(documents)):
        doc_vector = [term_matrix[term][doc_id] for term in term_matrix]
        intersection = sum(q * d for q, d in zip(query_vector, doc_vector))
        
        # Apply binary scoring, 1 if intersection > 0 else 0
        if intersection > 0:
            scores.append((doc_id + 1, 1))  # Relevant document
        else:
            scores.append((doc_id + 1, 0))  # Irrelevant document

    return scores


def non_overlapped_list_model(terms, documents):
    term_docs = {term: set() for term in terms}
    for doc_id, tokens in documents.items():
        for term in terms:
            if term in tokens:
                term_docs[term].add(doc_id)
    non_overlapping_docs = set()
    for doc_set in term_docs.values():
        non_overlapping_docs.update(doc_set)
    return list(non_overlapping_docs)

def expand_query(query):
    query_tokens = preprocess(query)
    expanded_terms = set(query_tokens)
    for token in query_tokens:
        if token in SYNONYMS:
            expanded_terms.update([synonym.lower() for synonym in SYNONYMS[token]])  # Ensure all terms are lowercase
    return list(expanded_terms)

def proximal_nodes_model(query, documents):
    expanded_query_terms = expand_query(query)
    relevant_docs = set()
    for doc_id, tokens in documents.items():
        # Compare terms in lowercase to ensure case-insensitivity
        if any(term in [t.lower() for t in tokens] for term in expanded_query_terms):
            relevant_docs.add(doc_id)
    return list(relevant_docs)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Document Retrieval GUI")
        self.setGeometry(100, 100, 800, 600)

        self.documents = {}
        self.file_mapping = {}

        # Hardcoded path to the documents directory
        self.folder_path = "./documents"  # Replace with your actual path

        # Load documents automatically on startup
        self.load_documents()

        layout = QVBoxLayout()

        # Input Section
        self.query_input = QLineEdit()
        self.query_input.setPlaceholderText("Enter your query here")
        self.query_input.setStyleSheet("font-size: 14px; padding: 10px; border-radius: 5px; border: 1px solid #ccc;")

        self.model_selector = QComboBox()
        self.model_selector.addItems(["Binary Independence Model", "Non-Overlapped List Model", "Proximal Nodes Model"])
        self.model_selector.setStyleSheet("font-size: 14px; padding: 10px;")

        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)
        self.result_display.setStyleSheet("font-size: 14px; padding: 10px; border-radius: 5px; border: 1px solid #ccc; background-color: #f9f9f9;")

        # Buttons
        self.run_button = QPushButton("Run Model")
        self.run_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.run_button.clicked.connect(self.run_model)

        # Layout setup
        layout.addWidget(QLabel("Enter Query:"))
        layout.addWidget(self.query_input)
        layout.addWidget(QLabel("Select Model:"))
        layout.addWidget(self.model_selector)
        layout.addWidget(self.run_button)
        layout.addWidget(QLabel("Results:"))
        layout.addWidget(self.result_display)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def load_documents(self):
        """ Load documents from the hardcoded folder path """
        if not os.path.exists(self.folder_path):
            QMessageBox.critical(self, "Error", f"Folder not found: {self.folder_path}")
            return

        try:
            self.documents, self.file_mapping = load_documents(self.folder_path)
            QMessageBox.information(self, "Success", "Documents loaded successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error loading documents: {str(e)}")

    def run_model(self):
        query = self.query_input.text().strip()
        if not query:
            QMessageBox.warning(self, "Warning", "Please enter a query.")
            return

        if not self.documents:
            QMessageBox.warning(self, "Warning", "No documents loaded.")
            return

        model = self.model_selector.currentText()
        results = ""
        try:
            if model == "Binary Independence Model":
                scores = binary_independence_model(query, self.documents)
                results = "\n".join(f"Document {self.file_mapping[doc_id]}: Score = {score:.2f}" for doc_id, score in scores)
            elif model == "Non-Overlapped List Model":
                terms = preprocess(query)
                doc_ids = non_overlapped_list_model(terms, self.documents)
                results = "\n".join(self.file_mapping[doc_id] for doc_id in doc_ids)
            elif model == "Proximal Nodes Model":
                doc_ids = proximal_nodes_model(query, self.documents)
                results = "\n".join(self.file_mapping[doc_id] for doc_id in doc_ids)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error running model: {str(e)}")
            return

        self.result_display.setText(results or "No results found.")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
