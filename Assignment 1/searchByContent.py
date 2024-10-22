import os

def readDocuments(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def searchContent(directory, query):
    matching_files = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            content = readDocuments(file_path)
            if content and query.lower() in content.lower():
                matching_files.append(filename)

    return matching_files

def main():
    directory = './documents'
    query = input("Enter the query to search for: ")
    matching_files = searchContent(directory, query)
    if matching_files:
        print("The following documents contain the query:")
        for file in matching_files:
            print(file)
    else:
        print("No documents contain the query.")

if __name__ == "__main__":
    main()
