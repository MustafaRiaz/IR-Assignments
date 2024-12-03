import os

def preprocess(text):
    # Convert text to lowercase and remove punctuation
    text = ''.join(c.lower() if c.isalnum() or c.isspace() else ' ' for c in text)
    return text.split()

def is_noun(word):
    # Assume words longer than 3 letters and not ending in common verb/adjective suffixes are nouns
    if len(word) <= 3:
        return False
    if word.endswith(('ing', 'ed', 'ly')):
        return False
    # Basic heuristic: filter out common short function words (articles, prepositions, etc.)
    common_non_nouns = {"the", "and", "a", "an", "in", "on", "at", "with", "for", "from", "to", "by"}
    if word in common_non_nouns:
        return False
    return True

def extract_nouns(text):
    words = preprocess(text)
    # Select words likely to be nouns based on heuristics
    nouns = [word for word in words if is_noun(word)]
    return nouns

def process_documents(directory="./documents"):
    # Dictionary to store nouns for each document
    document_nouns = {}

    # Iterate through each .txt file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            print(file_path)
            with open(file_path, "r") as file:
                content = file.read()
                nouns = extract_nouns(content)
                document_nouns[filename] = nouns
                print(f"Nouns in {filename}: {nouns}")

    return document_nouns

# Example usage
document_nouns = process_documents()
