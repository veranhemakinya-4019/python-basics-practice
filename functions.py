"""
Basic examples of Python functions.
Demonstrates function definition, parameters, and return values.
This file is intended for Python beginners.
"""

def greet(name: str) -> str:
    """
    Returns a greeting message for the given name.

    :param name: Name of the person to greet
    :return: A greeting string
    """
    return f"Hello, {name}!"


# Call the function and print the result
print(greet("Vera"))

# Example output:
# Hello, Vera!
