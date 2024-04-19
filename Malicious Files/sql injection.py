import sqlite3

def create_database():
    conn = sqlite3.connect("vulnerable.db")
    cursor = conn.cursor()

    # Create a table to store user data (vulnerable to SQL injection)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        )
    """)

    # Insert some sample data
    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
    cursor.execute("INSERT INTO users (username, password) VALUES ('user1', 'password1')")
    cursor.execute("INSERT INTO users (username, password) VALUES ('user2', 'password2')")

    conn.commit()
    conn.close()

def login(username, password):
    conn = sqlite3.connect("vulnerable.db")
    cursor = conn.cursor()

    # Vulnerable to SQL injection!
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)

    user = cursor.fetchone()
    conn.close()

    return user

if __name__ == "__main__":
    create_database()

    # Simulate user input (vulnerable to SQL injection)
    input_username = input("Enter your username: ")
    input_password = input("Enter your password: ")

    user_data = login(input_username, input_password)
    if user_data:
        print(f"Welcome, {user_data[1]}!")
    else:
        print("Invalid credentials. Please try again.")
