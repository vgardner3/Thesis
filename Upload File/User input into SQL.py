import sqlite3

# Connect to SQLite database (will create the database if it doesn't exist)
conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )
''')
conn.commit()

def add_user(name, email):
    # Insert user data into the database
    cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    print("User added successfully.")

def main():
    print("Welcome to the user data program!")
    while True:
        print("\n1. Add User")
        print("2. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter user's name: ")
            email = input("Enter user's email: ")
            add_user(name, email)
        elif choice == '2':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Close database connection
conn.close()
