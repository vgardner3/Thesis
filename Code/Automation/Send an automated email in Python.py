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




###Improve this code CHATGPT

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# Email configuration
sender_email = os.getenv("SENDER_EMAIL")  # Retrieve sender email from environment variable
receiver_email = os.getenv("RECEIVER_EMAIL")  # Retrieve receiver email from environment variable
password = os.getenv("EMAIL_PASSWORD")  # Retrieve email password from environment variable

def send_email(subject, body):
    """
    Send an email using SMTP.
    
    Args:
    - subject (str): Email subject.
    - body (str): Email body.
    """
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL(os.getenv("SMTP_SERVER"), os.getenv("SMTP_PORT")) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")

def register():
    """
    Register a new user.
    """
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    security_question = input("Enter your security question: ")
    security_answer = input("Enter your security answer: ")
    
    # Hash the password before storing it
    hashed_password = hash_password(password)
    
    # Store user information in a secure database (not implemented in this example)
    # In a real-world scenario, use a secure database instead of a dictionary
    user_database[username] = {'hashed_password': hashed_password, 'security_question': security_question, 'security_answer': security_answer}
    print("Registration successful!")

def hash_password(password):
    """
    Hash the password using a secure hashing algorithm.
    
    Args:
    - password (str): The password to hash.
    
    Returns:
    - str: The hashed password.
    """
    # In a real-world scenario, use a stronger hashing algorithm such as bcrypt
    # For demonstration purposes, we use a simple hash function
    return str(hash(password))

if __name__ == "__main__":
    # Example usage: sending email
    subject = "Automated Email Notification"
    body = """
    Hello,

    This is an automated email sent using Python.

    Regards,
    [Your Name]
    """
    send_email(subject, body)

    # Example usage: user registration
    register()
