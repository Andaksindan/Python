import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass
import base64

# Set up the SMTP server
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "piyushgdm@gmail.com"

# Prompt the user for the password
smtp_password = getpass.getpass(prompt="Enter your email password: ")

# Encode the password using base64
smtp_password_encoded = base64.b64encode(smtp_password.encode("utf-8")).decode("utf-8")

# Set up the message
msg = MIMEMultipart()
msg["From"] = "piyushgdm@gmail.com"
msg["To"] = "jerkycloud@gmail.com"
msg["Subject"] = "Test Email"
body = "This is a test email sent from Python."
msg.attach(MIMEText(body, "plain"))

# Send the message
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, base64.b64decode(smtp_password_encoded.encode("utf-8")).decode("utf-8"))
    server.sendmail(smtp_username, msg["To"], msg.as_string())

print("Email sent successfully!")
