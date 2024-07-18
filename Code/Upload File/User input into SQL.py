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

#####################
#improve this code
import sqlite3

class DatabaseManager:
    def __init__(self, db_name='user_data.db'):
        self.db_name = db_name
        self.conn = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def close(self):
        if self.conn:
            self.conn.close()

    def create_table(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    email TEXT
                )
            ''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def add_user(self, name, email):
        try:
            cursor = self.conn.cursor()
            cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
            self.conn.commit()
            print("User added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding user: {e}")

def main():
    db_manager = DatabaseManager()
    db_manager.connect()
    db_manager.create_table()
    
    print("Welcome to the user data program!")
    while True:
        print("\n1. Add User")
        print("2. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter user's name: ")
            email = input("Enter user's email: ")
            db_manager.add_user(name, email)
        elif choice == '2':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

    db_manager.close()

if __name__ == "__main__":
    main()
#


    # Create users table if it doesn't exist
    create_table(conn)
    
    print("Welcome to the user data program!")
    while True:
        print("\n1. Add User")
        print("2. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter user's name: ")
            email = input("Enter user's email: ")
            add_user(conn, name, email)
        elif choice == '2':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

    # Close database connection
    conn.close()

if __name__ == "__main__":
    main()
#

#########################
#Copilot make more secure
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
#
