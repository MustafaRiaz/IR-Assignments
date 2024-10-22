import os

def getAllTextDocuments():
    documents = []
    for file in os.listdir("documents"):
        if file.endswith(".txt"):
            with open(os.path.join("documents", file), "r", encoding="utf-8") as f:
                documents.append((file, f.read()))
    return documents

query = "java"

def preprocess(text):
    return set(text.lower().split())

def binary_vector(document, vocabulary):
    vector = []
    for term in vocabulary:
        if term in document:
            vector.append(1)
        else:
            vector.append(0)
    return vector

def jaccard_similarity(vector_a, vector_b):
    intersection = sum(1 for a, b in zip(vector_a, vector_b) if a == 1 and b == 1)
    union = sum(1 for a, b in zip(vector_a, vector_b) if a == 1 or b == 1)
    return intersection / union if union > 0 else 0

documents = getAllTextDocuments()
vocabulary = set()
for doc in documents:
    words = preprocess(doc[1])
    vocabulary.update(words)
vocabulary = list(vocabulary)

query_vector = binary_vector(preprocess(query), vocabulary)

document_vectors = []
for doc in documents:
    doc_id = doc[0]
    doc_vector = binary_vector(preprocess(doc[1]), vocabulary)
    document_vectors.append((doc_id, doc_vector))

scores = []
for doc_id, doc_vector in document_vectors:
    score = jaccard_similarity(query_vector, doc_vector)
    scores.append((doc_id, score))

scores = sorted(scores, key=lambda x: x[1], reverse=True)

top_k = 2
top_documents = scores[:top_k]
print("Top documents:", top_documents)
