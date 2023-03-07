import re

# Open the PDF file in binary mode
with open('Piyush_Gedam_resume.pdf', 'rb') as file:
    data = file.read()

# Use regular expressions to extract name and email
name_pattern = r'(?P<first_name>[A-Z][a-z]+)\s(?P<last_name>[A-Z][a-z]+)'
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
address_pattern = r'\b\d{1,5}\s+[\w\s]+\s+(?:Street|St\.|Road|Rd\.|Avenue|Ave\.|Boulevard|Blvd\.|Lane|Ln\.|Drive|Dr\.|Court|Ct\.|Circle|Cir\.|Way|Terrace|Ter\.|Place|Pl\.|Square|Sq\.|Parkway|Pkwy\.)[\s\w,]*\b'
phone_pattern = r'\b(?:\+?\d{1,2}\s*(?:[\-\.]|\s)\s*)?(?:\(\d{3}\)|\d{3})(?:\s*[\-\.]|\s)\d{3}(?:\s*[\-\.]|\s)\d{4}\b'
pincode_pattern = r'^[1-9][0-9]{5}$'


name = re.search(name_pattern, data.decode('latin-1'))
email = re.search(email_pattern, data.decode('latin-1'))
address = re.search(address_pattern, data.decode('latin-1'))
phone = re.search(phone_pattern, data.decode('latin-1'))
pincode = re.search(pincode_pattern, data.decode('latin-1'))
# utf-8 and ascii doesnt work so i tried latin-1 and its working jus fine

# Print the results
print(f"Name: {name.group(0)}")
print(f"Email: {email.group(0)}")
print(f"Address: {address}")
print(f"Phone: {phone.group(0)}")
print(f"Pincode: {pincode}")