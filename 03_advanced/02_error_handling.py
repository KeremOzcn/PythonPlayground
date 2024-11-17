try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
    # Tries to convert the user input to an integer.
except ValueError:
    # This block runs if the input is not a valid number.
    print("That's not a valid number!")
