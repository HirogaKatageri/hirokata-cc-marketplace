#!/usr/bin/env python3
"""
Tests for Hello World Program

This module contains unit tests for the hello_world.py program.
It demonstrates how to test even simple programs to ensure they work correctly.

Tests verify:
- The main() function produces the correct output
- The GREETING_MESSAGE constant has the expected value

Run tests with:
    python -m unittest test_hello_world.py
    or
    python -m unittest test_hello_world.py -v (for verbose output)
"""

import unittest
import io
import sys
from hello_world import main, GREETING_MESSAGE


class TestHelloWorld(unittest.TestCase):
    """Test cases for Hello World program."""

    def test_main_output(self):
        """
        Test that main() prints the correct greeting message.

        This test captures stdout (the console output) to verify that
        the main() function prints exactly "Hello, World!" followed by
        a newline character.
        """
        # Capture stdout by redirecting it to a StringIO object
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Call the main function
        main()

        # Restore stdout to its original state
        sys.stdout = sys.__stdout__

        # Verify the output matches our expectation
        # Note: print() adds a newline (\n) at the end
        self.assertEqual(captured_output.getvalue(), "Hello, World!\n")

    def test_greeting_message_constant(self):
        """
        Test that GREETING_MESSAGE has the correct value.

        This test verifies that the constant is defined with the
        expected value. While simple, this ensures that if the constant
        is accidentally changed, tests will catch it.
        """
        self.assertEqual(GREETING_MESSAGE, "Hello, World!")


if __name__ == "__main__":
    # This allows running the tests directly: python test_hello_world.py
    unittest.main()
