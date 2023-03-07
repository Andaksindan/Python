import re
import PyPDF2
import pandas as pd

# Open the PDF file
with open('resume-sample.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Get the text content of the PDF
    resume_text = ''
    for page in pdf_reader.pages:
        resume_text += page.extract_text()

    # Define the regular expression patterns
    name_pattern = re.compile(r'(?P<first_name>[A-Z][a-z]+)\s(?P<last_name>[A-Z][a-z]+)')
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    phone_pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
    pincode_pattern = re.compile(r'^[1-9][0-9]{6}$')

    # Search for the name and email address
    name_match = name_pattern.search(resume_text)
    email_match = email_pattern.search(resume_text)
    phone_match = re.search(phone_pattern, resume_text)
    pincode_match = pincode_pattern.search(resume_text)

    # Create a DataFrame from the results
    data = {'Name': '', 'Email': '', 'Phone': '', 'Pincode': ''}
    if name_match:
        data['Name'] = '{} {}'.format(name_match.group('first_name'), name_match.group('last_name'))
    if email_match:
        data['Email'] = email_match.group()
    if phone_match:
        data['Phone'] = phone_match.group()
    if pincode_match:
        data['Pincode'] = pincode_match.group()
    df = pd.DataFrame(data, index=[0])

    # Save the results to an Excel file
    df.to_excel('resume_results.xlsx', index=False)
