with open("example.txt", "w") as file:
    file.write("This is an example file.")
    # Opens a file in write mode and writes a line of text.

with open("example.txt", "r") as file:
    content = file.read()
    # Opens the file in read mode and reads its content.
    print(content)
    # Prints the content of the file.