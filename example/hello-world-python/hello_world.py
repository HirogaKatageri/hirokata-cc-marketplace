#!/usr/bin/env python3
# The shebang line above tells Unix-like systems to run this file with Python 3
# This allows direct execution with ./hello_world.py (after chmod +x)
# Windows systems ignore this line, so it doesn't affect compatibility

"""
Hello World Program

A simple Python program that demonstrates basic output functionality.
This program prints a greeting message to the console.

Usage:
    python hello_world.py
    or
    ./hello_world.py (on Unix-like systems)
"""

# Constants
# Using a constant instead of hardcoding "Hello, World!" in the print statement
# demonstrates good practice: it makes the message easy to change and reuse
GREETING_MESSAGE = "Hello, World!"


def main():
    """
    Main entry point for the Hello World program.

    This function is the core of the program. Separating the main logic
    into a function (rather than putting code directly in the module)
    makes the code more testable and reusable.

    Prints the greeting message to standard output.
    """
    print(GREETING_MESSAGE)


# The "main guard" pattern below is a Python best practice
# It ensures main() only runs when this file is executed directly,
# not when it's imported as a module in another program
if __name__ == "__main__":
    main()
