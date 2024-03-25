# File Creation
def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line with some text and numbers: 98765\n")
        print("File 'my_file.txt' created successfully with initial content.")
    except Exception as e:
        print("An error occurred while creating the file:", e)


# File Reading and Display
def read_file():
    try:
        with open("my_file.txt", "r") as file:
            contents = file.read()
            print("Contents of my_file.txt:")
            print(contents)
    except FileNotFoundError:
        print("File 'my_file.txt' not found.")
    except PermissionError:
        print("Permission denied to read the file.")
    except Exception as e:
        print("An error occurred while reading the file:", e)


# File Appending
def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending line 1\n")
            file.write("Appending line 2\n")
            file.write("Appending line 3\n")
        print("Three lines appended to my_file.txt.")
    except FileNotFoundError:
        print("File 'my_file.txt' not found.")
    except PermissionError:
        print("Permission denied to append to the file.")
    except Exception as e:
        print("An error occurred while appending to the file:", e)


if __name__ == "__main__":
    create_file()
    read_file()
    append_to_file()
    read_file()  # Display updated content after appending