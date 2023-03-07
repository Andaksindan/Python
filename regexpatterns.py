import re

# A custom regex pattern for matching email addresses
EMAIL_PATTERN = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
name_pattern = re.compile(r'(?P<first_name>[A-Z][a-z]+)\s(?P<last_name>[A-Z][a-z]+)')
phone_pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
pincode_pattern = re.compile(r'^[1-9][0-9]{5}$')




# ---------------------------------------------------------------------#
# name_pattern = r'(?i)\b(?:[A-Z]\.)+ [A-Z][a-z]+(?: [A-Z][a-z]+)*\b'
# email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# address_pattern = r'\b\d{1,5}\s+[\w\s]+\s+(?:Street|St\.|Road|Rd\.|Avenue|Ave\.|Boulevard|Blvd\.|Lane|Ln\.|Drive|Dr\.|Court|Ct\.|Circle|Cir\.|Way|Terrace|Ter\.|Place|Pl\.|Square|Sq\.|Parkway|Pkwy\.)[\s\w,]*\b'
# phone_pattern = r'\b(?:\+?\d{1,2}\s*(?:[\-\.]|\s)\s*)?(?:\(\d{3}\)|\d{3})(?:\s*[\-\.]|\s)\d{3}(?:\s*[\-\.]|\s)\d{4}\b'
# pincode_pattern = r'^[1-9][0-9]{5}$'
