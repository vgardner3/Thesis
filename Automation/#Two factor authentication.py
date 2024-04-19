#Two factor authentication with a security question
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in user_database and user_database[username]['password'] == password:
        # Password authentication successful, now ask security question
        security_question = user_database[username]['security_question']
        security_answer = user_database[username]['security_answer']
        user_answer = input(security_question + ": ")

        if user_answer == security_answer:
            print("Login successful!")
        else:
            print("Incorrect answer to security question. Login failed.")
    else:
        print("Invalid username or password. Login failed.")

def main():
    print("1. Register")
    print("2. Login")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        register()
    elif choice == '2':
        login()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()


##Make this code more secure CHATGPT
import hashlib

user_database = {}  # Example user database (username -> {hashed_password, security_question, hashed_security_answer})

def hash_password(password):
    """Hashes the password using a secure hashing algorithm."""
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    security_question = input("Choose a security question: ")
    security_answer = input("Enter the answer to your security question: ")

    # Store hashed password and hashed security answer
    hashed_password = hash_password(password)
    hashed_security_answer = hash_password(security_answer)

    user_database[username] = {
        'hashed_password': hashed_password,
        'security_question': security_question,
        'hashed_security_answer': hashed_security_answer
    }
    print("Registration successful!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in user_database:
        stored_password = user_database[username]['hashed_password']
        if stored_password == hash_password(password):
            # Password authentication successful, now ask security question
            security_question = user_database[username]['security_question']
            security_answer = user_database[username]['hashed_security_answer']
            user_answer = input(security_question + ": ")

            if user_answer == security_answer:
                print("Login successful!")
                return
            else:
                print("Incorrect answer to security question. Login failed.")
                return

    print("Invalid username or password. Login failed.")

def main():
    print("1. Register")
    print("2. Login")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        register()
    elif choice == '2':
        login()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
