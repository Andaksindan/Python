from regexpatterns import EMAIL_PATTERN

# Use the EMAIL_PATTERN to match an email address
# name = 'John Doe'
# if name_pattern.match(name):
#     print('Valid name')
# else:
#     print('Invalid name')


# from regexpatterns import email_pattern


email = 'pacfuac@gmail.com'
if EMAIL_PATTERN.match(email):
    print('Valid Email')
else:
    print('Invalid Email')