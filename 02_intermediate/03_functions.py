def greet(name):
    # Defines a function that takes a name as a parameter.
    return f"Hello, {name}!"
    # Returns a greeting message with the given name.

user_name = input("What is your name? ")
# Gets the user's name as input.
print(greet(user_name))
# Calls the function and prints the returned greeting.