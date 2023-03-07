import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from cred import sender__email
from cred import receiver__email
from cred import passwordd
from cred import subjectt
from cred import messagee


# Define email details
sender_email = sender__email
receiver_email = receiver__email
password = passwordd
subject = subjectt
message = messagee

# Create message object
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

# Create SMTP session with SSL/TLS encryption
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

# Login to email account
server.login(sender_email, password)

# Send email
server.sendmail(sender_email, receiver_email, msg.as_string())

# Terminate the SMTP session
server.quit()
