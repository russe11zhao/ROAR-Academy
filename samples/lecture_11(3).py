import PyPDF2 

frequency_table = dict()
file_handle = open('Sense-and-Sensibility-by-Jane-Austen.pdf', 'rb') 
pdfReader = PyPDF2.PdfReader(file_handle) 
page_number = len(pdfReader.pages)# this tells you total pages 

for i in range(page_number):
    page_object = pdfReader.pages[i]    # We just get page 0 as example 
    page_text = page_text + page_object.extractText()   # this is the str type of full page

page_lines = page_text.split('\n')
page_words = page_lines.split()

def remove_symbols_from_word(word):
    # Remove non-alphabetic characters from the word
    return re.sub(r'[^a-zA-Z]', '', word) #remove symbol with function from re

words_no_puntuation = [remove_symbols_from_word(word) for word in page_words]
print(words_no_puntuation)

for word in page_words:
    if word.isalpha():
        if word != 'CHAPTER'and word != 'page':
            word = word.lower()
            if word in frequency_table:
                frequency_table[word] += 1
            else:
                frequency_table[word] = 1

for key in frequency_table:
    print(key, end=' ')
print()
for key in frequency_table:
    print(frequency_table[key], end=" ")
