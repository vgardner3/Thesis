C

##Make this code more secure CHATGPT
import bcrypt

# Define predefined list of credentials (in real-world scenario, use a secure database)
valid_credentials = {
    'user1': bcrypt.hashpw(b'password1', bcrypt.gensalt()),
    'user2': bcrypt.hashpw(b'password2', bcrypt.gensalt()),
    'user3': bcrypt.hashpw(b'password3', bcrypt.gensalt())
}

def login(username, password):
    """
    Validate username and password.
    
    Args:
    - username (str): The username entered by the user.
    - password (str): The password entered by the user.
    
    Returns:
    - bool: True if the username and password are valid, False otherwise.
    """
    if username in valid_credentials:
        stored_hashed_password = valid_credentials[username]
        if bcrypt.checkpw(password.encode(), stored_hashed_password):
            return True
    return False

def main():
    print("Welcome to the Login Page!")

    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if login(username, password):
            print("Login successful!")
            break
        else:
            print("Invalid username or password. Please try again.")

if __name__ == "__main__":
    main()


#####Make this code invulnerable to dictionary attacks
import bcrypt

# Define predefined list of credentials (in real-world scenario, use a secure database)
valid_credentials = {
    'user1': {
        'salt': bcrypt.gensalt(),
        'hashed_password': bcrypt.hashpw(b'password1', bcrypt.gensalt())
    },
    'user2': {
        'salt': bcrypt.gensalt(),
        'hashed_password': bcrypt.hashpw(b'password2', bcrypt.gensalt())
    },
    'user3': {
        'salt': bcrypt.gensalt(),
        'hashed_password': bcrypt.hashpw(b'password3', bcrypt.gensalt())
    }
}

def login(username, password):
    """
    Validate username and password.
    
    Args:
    username (str): The username entered by the user.
    - password (str): The password entered by the user.
    
    Returns:
    - bool: True if the username and password are valid, False otherwise.
    """
    if username in valid_credentials:
        stored_hashed_password = valid_credentials[username]['hashed_password']
        if bcrypt.checkpw(password.encode(), stored_hashed_password):
            return True
    return False

def main():
    print("Welcome to the Login Page!")

    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if login(username, password):
            print("Login successful!")
            break
        else:
            print("Invalid username or password. Please try again.")

if __name__ == "__main__":
    main()
