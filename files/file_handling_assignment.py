# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("This is the first line\n")
        file.write("here are the numbers 12345\n")
        file.write("0795555775\n")
except PermissionError:
    print("Permission denied while trying to create the file.")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        for line in file:
            print(line.strip())  # Remove newline characters before printing
except FileNotFoundError:
    print("File not found.")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Appending another line \n")
        file.write("67890\n")
        file.write("final but not least \n")
except PermissionError:
    print("Permission denied while trying to append to the file.")
except FileNotFoundError:
    print("File not found.")
finally:
    print("File operations completed.")
