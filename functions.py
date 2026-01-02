"""
Basic examples of Python functions.
Demonstrates function definition, parameters, and return values.
This file is intended for Python beginners.
"""

# Define a function that returns a greeting message
def greet(name: str) -> str:
    # Format and return the greeting using an f-string
    return f"Hello, {name}!"


# Call the function and display the result
print(greet("Vera"))

# Example output:
# Hello, Vera!
