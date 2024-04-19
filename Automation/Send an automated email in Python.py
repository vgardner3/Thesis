#Send an automated email in Python 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
sender_email = "your_email@example.com"
receiver_email = "recipient_email@example.com"
password = "your_email_password"

# Create message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Automated Email Notification"

body = """
Hello,

This is an automated email sent using Python.

Regards,
[Your Name]
"""

message.attach(MIMEText(body, "plain"))

# Connect to SMTP server and send email
try:
    with smtplib.SMTP_SSL("smtp.example.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email. Error: {str(e)}")

import random

# Database to store user information (in real-world scenarios, you would use a proper database)
user_database = {}

def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    security_question = input("Enter your security question: ")
    security_answer = input("Enter your security answer: ")
    user_database[username] = {'password': password, 'security_question': security_question, 'security_answer': security_answer}
    print("Registration successful!")
