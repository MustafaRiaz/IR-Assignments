import os
import math

STOPWORDS={
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
    documents=[]
    for file in os.listdir("documents"):
        if file.endswith(".txt"):
            with open(os.path.join("documents", file), "r", encoding="utf-8") as f:
                documents.append((file, f.read()))
    return documents

def preprocess(text):
    words=text.lower().split()
    processed=[]
    for word in words:
        cleaned_word=word.strip('.,!?";:()[]')
        if cleaned_word not in STOPWORDS:
            processed.append(cleaned_word)
    return processed

def TermFrequency(query, document_content):
    words=preprocess(document_content)
    query_count=words.count(query.lower())
    return query_count / len(words) if len(words) > 0 else 0

def InverseDocumentFrequency(query, documents):
    query=query.lower()
    count=0
    for _, doc_content in documents:
        words=preprocess(doc_content)
        if query in words:
            count+=1
    N=len(documents)
    idf_value=math.log(N / (count + 1))
    return idf_value

def TFIDF(query, document_content, idf):
    tf=TermFrequency(query, document_content)
    return tf * idf

if __name__ == "__main__":
    documents=getAllTextDocuments()
    query="Python"
    idf=InverseDocumentFrequency(query, documents)
    print(f"IDF for '{query}': {idf:.4f}")
    found_in_documents=[]
    
    for doc_name, doc_content in documents:
        tfidf=TFIDF(query, doc_content, idf)

        if tfidf > 0:
            found_in_documents.append(doc_name)
            print(f"Document '{doc_name}': TF-IDF={tfidf:.4f}")
    
    if found_in_documents:
        print("\nQuery found in the following documents:")
        for doc_name in found_in_documents:
            print(f"- {doc_name}")
    else:
        print("\nQuery not found in any documents.")
