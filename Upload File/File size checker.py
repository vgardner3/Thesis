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
