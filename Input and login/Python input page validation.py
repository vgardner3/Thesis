def login(username, password):
    """
    Validate username and password.
    
    Args:
    - username (str): The username entered by the user.
    - password (str): The password entered by the user.
    
    Returns:
    - bool: True if the username and password are valid, False otherwise.
    """
    # Define predefined list of credentials (in real-world scenario, use a secure database)
    valid_credentials = {
        'user1': 'password1',
        'user2': 'password2',
        'user3': 'password3'
    }
    
    if username in valid_credentials and valid_credentials[username] == password:
        return True
    else:
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
