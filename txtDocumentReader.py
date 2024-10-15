


def searchWord(filePath, word):
    try:
        with open(filePath, 'r') as file:
            lines = file.readlines()
            found_lines = []
            for line_num, line in enumerate(lines, 1):
                if word.lower() in line.lower():
                    found_lines.append((line_num, line.strip()))
            return found_lines
    except FileNotFoundError:
        return f"Error: The file '{filePath}' does not exist."

filePath = 'sample.txt'
word = input("Enter the word to search: ")
results = searchWord(filePath, word)

if results:
    print(f"Word '{word}' found in the following lines:")
    for line_num, line in results:
        print(f"Line {line_num}: {line}")
else:
    print(f"The word '{word}' was not found in the document.")
