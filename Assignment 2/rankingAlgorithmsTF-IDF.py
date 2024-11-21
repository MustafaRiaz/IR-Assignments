import os
import math
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

STOPWORDS = {
    "a", "an", "the", "and", "or", "but", "if", "while", "for", "with",
    "about", "against", "between", "into", "through", "during", "before",
    "after", "above", "below", "to", "from", "up", "down", "in", "out",
    "on", "off", "over", "under", "again", "further", "then", "once",
    "here", "there", "when", "where", "why", "how", "all", "any", "both",
    "each", "few", "more", "most", "other", "some", "such", "no", "nor",
    "not", "only", "own", "same", "so", "than", "too", "very", "can",
    "will", "just", "don't", "should", "now"
}

def getAllTextDocuments():
    documents = []
    if not os.path.exists("documents"):
        os.makedirs("documents")
    for file in os.listdir("documents"):
        if file.endswith(".txt"):
            with open(os.path.join("documents", file), "r", encoding="utf-8") as f:
                documents.append((file, f.read()))
    return documents

def preprocess(text):
    words = text.lower().split()
    processed = [word.strip('.,!?";:()[]') for word in words if word not in STOPWORDS]
    return processed

def term_frequency(word, words):
    return words.count(word) / len(words) if len(words) > 0 else 0

def inverse_document_frequency(word, documents):
    count = sum(1 for _, doc_content in documents if word in preprocess(doc_content))
    N = len(documents)
    return math.log(N / (count + 1)) if count > 0 else 0

def compute_tf_idf(query_terms, document, documents):
    words = preprocess(document)
    tf_idf_vector = {}
    for term in query_terms:
        tf = term_frequency(term, words)
        idf = inverse_document_frequency(term, documents)
        tf_idf_vector[term] = tf * idf
    return tf_idf_vector

def cosine_similarity(vector1, vector2):
    dot_product = sum(vector1.get(term, 0) * vector2.get(term, 0) for term in vector1.keys())
    magnitude1 = math.sqrt(sum(val ** 2 for val in vector1.values()))
    magnitude2 = math.sqrt(sum(val ** 2 for val in vector2.values()))
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    return dot_product / (magnitude1 * magnitude2)

class TFIDFApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TF-IDF Query Tool")
        self.root.geometry("800x600")
        self.root.configure(bg="#fafafa")

        # Header
        header = tk.Label(
            root, text="Search Tool (TF-IDF & Cosine Similarity)", bg="#fafafa", fg="#833AB4",
            font=("Helvetica", 20, "bold")
        )
        header.pack(pady=20)

        # Query Frame
        query_frame = tk.Frame(root, bg="#fafafa")
        query_frame.pack(pady=10)

        query_label = tk.Label(query_frame, text="Enter Query:", bg="#fafafa", font=("Helvetica", 14))
        query_label.grid(row=0, column=0, padx=5, pady=5)

        self.query_entry = tk.Entry(query_frame, font=("Helvetica", 14), width=40)
        self.query_entry.grid(row=0, column=1, padx=5, pady=5)

        self.method_var = tk.StringVar(value="TF-IDF")
        method_menu = ttk.OptionMenu(query_frame, self.method_var, "TF-IDF", "TF-IDF", "Cosine Similarity")
        method_menu.grid(row=0, column=2, padx=5, pady=5)

        search_button = ttk.Button(query_frame, text="Search", command=self.search_query)
        search_button.grid(row=0, column=3, padx=5, pady=5)

        # Results Frame
        results_frame = tk.Frame(root, bg="#fafafa")
        results_frame.pack(fill=tk.BOTH, expand=True, pady=10, padx=20)

        self.results_text = tk.Text(results_frame, font=("Helvetica", 12), wrap=tk.WORD, state=tk.DISABLED, bg="#f0f0f0")
        self.results_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def search_query(self):
        query = self.query_entry.get().strip()
        if not query:
            messagebox.showwarning("Input Error", "Please enter a query.")
            return

        documents = getAllTextDocuments()
        if not documents:
            messagebox.showwarning("No Documents", "No text documents found in the 'documents' folder.")
            return

        query_terms = preprocess(query)
        method = self.method_var.get()
        results = []

        if method == "TF-IDF":
            for doc_name, doc_content in documents:
                tf_idf_vector = compute_tf_idf(query_terms, doc_content, documents)
                score = sum(tf_idf_vector.values())
                if score > 0:
                    results.append((doc_name, score))
            results.sort(key=lambda x: x[1], reverse=True)
            results_text = [f"Document: {doc_name} | Score: {score:.4f}" for doc_name, score in results]

        elif method == "Cosine Similarity":
            query_vector = compute_tf_idf(query_terms, " ".join(query_terms), documents)
            for doc_name, doc_content in documents:
                doc_vector = compute_tf_idf(query_terms, doc_content, documents)
                similarity = cosine_similarity(query_vector, doc_vector)
                if similarity > 0:
                    results.append((doc_name, similarity))
            results.sort(key=lambda x: x[1], reverse=True)
            results_text = [f"Document: {doc_name} | Similarity: {similarity:.4f}" for doc_name, similarity in results]

        self.display_results(query, results_text)

    def display_results(self, query, results_text):
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete("1.0", tk.END)

        if results_text:
            self.results_text.insert(tk.END, f"Query: {query}\n\n")
            self.results_text.insert(tk.END, "\n".join(results_text))
        else:
            self.results_text.insert(tk.END, f"No results found for query: {query}")

        self.results_text.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = TFIDFApp(root)
    root.mainloop()
