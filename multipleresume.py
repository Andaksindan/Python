import os
import re
import PyPDF2

# Define the regex patterns you want to extract
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
phone_pattern = r'(\d{3})[-. ]?(\d{3})[-. ]?(\d{4})'

# Define the directory where the resumes are stored
resume_directory = "Resume"

# Loop through all the PDF files in the directory
for filename in os.listdir(resume_directory):
    if filename.endswith('.pdf'):
        # Open the PDF file and read its contents
        with open(os.path.join(resume_directory, filename), 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            resume_text = ''
            for page in range(pdf_reader.getNumPages()):
                resume_text += pdf_reader.getPage(page).extractText()

        # Apply regex pattern matching to the resume text
        email_matches = re.findall(email_pattern, resume_text)
        phone_matches = re.findall(phone_pattern, resume_text)

        # Print the results
        print(f'{filename}:')
        print(f'Email addresses: {", ".join(email_matches)}')
        print(f'Phone numbers: {", ".join("".join(phone) for phone in phone_matches)}')
