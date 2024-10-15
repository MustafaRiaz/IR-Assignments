import os
import math

# Define a set of common English stopwords
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
    for file in os.listdir("documents"):
        if file.endswith(".txt"):
            with open(os.path.join("documents", file), "r", encoding="utf-8") as f:
                documents.append((file, f.read()))
    return documents

def preprocess(text):
    # Convert text to lowercase and split into words
    words = text.lower().split()
    # Remove punctuation and stopwords
    processed = [word.strip('.,!?";:()[]') for word in words if word.strip('.,!?";:()[]') not in STOPWORDS]
    return processed

def TermFrequency(query, document_content):
    words = preprocess(document_content)
    query_count = words.count(query.lower())
    return query_count / len(words) if len(words) > 0 else 0

def InverseDocumentFrequency(query, documents):
    query = query.lower()
    count = 0
    for _, doc_content in documents:
        words = preprocess(doc_content)
        if query in words:
            count += 1

    if count == 0:
        return 0
    return math.log(len(documents) / count)

def TFIDF(query, document_content, documents):
    tf = TermFrequency(query, document_content)
    idf = InverseDocumentFrequency(query, documents)
    return tf * idf

if __name__ == "__main__":
    documents = getAllTextDocuments()
    query = "Python"  # Change the query term here
    found_in_documents = []
    
    for doc_name, doc_content in documents:
        tf = TermFrequency(query, doc_content)
        tfidf = TFIDF(query, doc_content, documents)

        if tf > 0:
            found_in_documents.append(doc_name)
            print(f"Document '{doc_name}': TF = {tf:.4f}, TF-IDF = {tfidf:.4f}")
    
    if found_in_documents:
        print("\nQuery found in the following documents:")
        for doc_name in found_in_documents:
            print(f"- {doc_name}")
    else:
        print("\nQuery not found in any documents.")
