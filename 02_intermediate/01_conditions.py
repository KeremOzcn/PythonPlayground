number = int(input("Enter a number: "))
# Gets a number input from the user and converts it to an integer.

if number > 0:
    print("The number is positive.")
    # This block runs if the number is greater than 0.
elif number < 0:
    print("The number is negative.")
    # This block runs if the number is less than 0.
else:
    print("The number is zero.")
    # This block runs if the number is exactly 0.