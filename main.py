import PyPDF2
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

pdf_file = open('Piyush_Gedam_resume.pdf', 'rb')
try:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
except PyPDF2.utils.PdfReadError as e:
    print("Error: Could not read PDF file.")
    print(e)
    exit()

text = ''
for page in range(pdf_reader.getNumPages()):
    text += pdf_reader.getPage(page).extractText()

tokens = word_tokenize(text)
stop_words = set(stopwords.words('english'))
stop_words.update(string.punctuation)
filtered_tokens = [word.lower() for word in tokens if not word.lower() in stop_words]

nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

ner_tags = nltk.ne_chunk(nltk.pos_tag(filtered_tokens))
key_points = set([])
for chunk in ner_tags:
    if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
        key_points.add(' '.join(c[0] for c in chunk.leaves()))

pdf_file.close() # Always close the file when done
