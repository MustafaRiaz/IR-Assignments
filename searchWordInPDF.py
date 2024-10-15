import PyPDF2

def getTextFromPDF(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        return text

def searchWord(file_path, search_word):
    pdf_text = getTextFromPDF(file_path)
    if pdf_text is None:
        return []
    lines = pdf_text.split('\n')
    found_lines = []
    for line_num, line in enumerate(lines, 1):
        if search_word.lower() in line.lower():
            found_lines.append((line_num, line.strip()))
    return found_lines

file_path = 'sample.pdf'
search_word = input("Enter the word to search: ")
results = searchWord(file_path, search_word)

if results:
    print(f"Word '{search_word}' found in the following lines:")
    for line_num, line in results:
        print(f"Line {line_num}: {line}")
else:
    print(f"The word '{search_word}' was not found in the document.")
