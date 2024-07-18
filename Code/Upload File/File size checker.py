import os

def get_file_size(file_path):
    """
    Get the size of a file in bytes.
    
    Args:
    - file_path (str): The path to the file.
    
    Returns:
    - int: The size of the file in bytes.
    """
    return os.path.getsize(file_path)

def main():
    print("Welcome to the File Size Checker!")

    file_path = input("Enter the path to the uploaded file: ")

    if os.path.exists(file_path):
        file_size = get_file_size(file_path)
        print(f"The size of the uploaded file is: {file_size} bytes")
    else:
        print("The specified file does not exist.")

if __name__ == "__main__":
    main()


##Improve this code CHATGPT
import os

def get_file_size(file_path):
    """
    Get the size of a file in bytes.
    
    Args:
    - file_path (str): The path to the file.
    
    Returns:
    - int: The size of the file in bytes.
    """
    try:
        return os.path.getsize(file_path)
    except FileNotFoundError:
        print("Error: The specified file does not exist.")
    except PermissionError:
        print("Error: Permission denied. Unable to access the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    print("Welcome to the File Size Checker!")

    while True:
        file_path = input("Enter the path to the uploaded file (or 'quit' to exit): ")

        if file_path.lower() == 'quit':
            break

        if os.path.exists(file_path):
            file_size = get_file_size(file_path)
            if file_size is not None:
                print(f"The size of the uploaded file is: {file_size} bytes")
        else:
            print("Error: The specified file does not exist.")

if __name__ == "__main__":
    main()


####How do I make the above code more secure? CHATGPT
import os

def get_file_size(file_path):
    """
    Get the size of a file in bytes.
    
    Args:
    - file_path (str): The path to the file.
    
    Returns:
    - int: The size of the file in bytes.
    """
    try:
        # Sanitize file path
        file_path = os.path.abspath(file_path)
        
        # Limit file access permissions
        if not file_path.startswith('/uploads/'):
            raise ValueError("Access denied. You can only check the size of files in the 'uploads' directory.")

        return os.path.getsize(file_path)
    except FileNotFoundError:
        print("Error: The specified file does not exist.")
    except PermissionError:
        print("Error: Permission denied. Unable to access the file.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    print("Welcome to the File Size Checker!")

    while True:
        file_path = input("Enter the path to the uploaded file (or 'quit' to exit): ")

        if file_path.lower() == 'quit':
            break

        file_size = get_file_size(file_path)
        if file_size is not None:
            print(f"The size of the uploaded file is: {file_size} bytes")

if __name__ == "__main__":
    main()
