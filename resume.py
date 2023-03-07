import re
import PyPDF2

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
    pincode_pattern = re.compile(r'^[1-9][0-9]{5}$')


    # Search for the name and email address
    name_match = name_pattern.search(resume_text)
    email_match = email_pattern.search(resume_text)
    phone_match = re.search(phone_pattern, resume_text)
    pincode_match = pincode_pattern.search(resume_text)

    # Print the results
    if name_match:
        print('Name: {} {}'.format(name_match.group('first_name'), name_match.group('last_name')))
    else:
        print('Name not found')
    
    if email_match:
        print('Email: {}'.format(email_match.group()))
    else:
        print('Email not found')

    if phone_match:
        print('Phone: {}'.format(phone_match.group()))
    else:
        print('Phone not found')

    if pincode_match:
        print('Pincode: {}' .format(pincode_match.group()))
    else:
        print('Pincode not match')    