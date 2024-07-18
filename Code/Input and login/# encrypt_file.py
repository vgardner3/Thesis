"""# encrypt_file.py

import pyAesCrypt

def encrypt_file(input_file, output_file, password):
    buffer_size = 64 * 1024  # 64KB buffer size

    try:
        with open(input_file, 'rb') as infile:
            with open(output_file, 'wb') as outfile:
                pyAesCrypt.encryptStream(infile, outfile, password, buffer_size)
        print(f"File '{input_file}' encrypted successfully to '{output_file}'.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    input_file = "your_file.txt"  # Replace with the path to your input file
    output_file = "encrypted_file.aes"  # Output encrypted file
    password = "your_secret_password"  # Replace with your desired password

    encrypt_file(input_file, output_file, password)"""

## Make this code more secure CHATGPT
import os
import pyAesCrypt

from hashlib import pbkdf2_hmac

def encrypt_file(input_file, output_file, password, salt_length=16, key_length=32):
    buffer_size = 64 * 1024  # 64KB buffer size

    try:
        # Generate a salt
        salt = os.urandom(salt_length)

        # Derive encryption key from password and salt using PBKDF2
        key = pbkdf2_hmac('sha256', password.encode(), salt, 100000, dklen=key_length)

        # Encrypt the file using AES encryption (CBC mode)
        pyAesCrypt.encryptFile(input_file, output_file, key, buffer_size)

        print(f"File '{input_file}' encrypted successfully to '{output_file}'.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    input_file = "input.txt"  # Replace with the path to your input file
    output_file = "encrypted_file.aes"  # Output encrypted file
    password = "Cyber3!"  # Replace with your desired password

    encrypt_file(input_file, output_file, password)
