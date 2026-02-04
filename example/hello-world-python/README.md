# Hello World Python Program

A simple, well-structured Hello World program in Python that demonstrates professional development practices and serves as an educational template for beginners.

## Description

This project implements a classic "Hello, World!" program in Python. While simple in functionality, it demonstrates fundamental Python concepts and professional development practices that scale to larger projects.

### What You'll Learn

This beginner-friendly program demonstrates:
- **Basic Project Structure**: How to organize a Python project properly
- **Function Definitions**: Creating reusable functions with clear purposes
- **Docstrings and Comments**: Documenting code for clarity and maintainability
- **The Main Guard Pattern**: Using `if __name__ == "__main__":` for script entry points
- **Constants vs Magic Strings**: Using named constants instead of hardcoded values
- **Cross-Platform Script Execution**: Making scripts work on Windows, macOS, and Linux
- **PEP 8 Style Compliance**: Following Python's official style guide
- **Testing Basics**: Verifying program behavior with unit tests
- **Professional Documentation**: Creating clear, comprehensive project documentation

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer, usually included with Python)
- Git (optional, for version control)

To check your Python version:
```bash
python --version
```

If Python is not installed, download it from [python.org](https://www.python.org/downloads/).

## Installation

1. Clone or download this project:
```bash
cd hello-world-python
```

2. (Optional but recommended) Create and activate a virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate on macOS/Linux
source venv/bin/activate

# Activate on Windows
venv\Scripts\activate
```

3. Install dependencies (none required for this project):
```bash
pip install -r requirements.txt
```

## Usage

There are two ways to run the program:

### Method 1: Using Python interpreter (all platforms)

```bash
python hello_world.py
```

This method works on all platforms (Windows, macOS, Linux) and is the most portable.

### Method 2: Direct execution (macOS/Linux only)

First, make the script executable (one-time setup):
```bash
chmod +x hello_world.py
```

Then run it directly:
```bash
./hello_world.py
```

**Note**: Method 2 doesn't work on Windows. Windows users should use Method 1.

### Expected Output

Both methods produce the same output:
```
Hello, World!
```

## Testing

This project includes unit tests to verify correct behavior. Run the test suite using Python's built-in unittest framework:

```bash
python -m unittest test_hello_world.py
```

Or run with verbose output to see detailed test results:

```bash
python -m unittest test_hello_world.py -v
```

Expected test output:
```
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

## Project Structure

```
hello-world-python/
├── .gitignore              # Git ignore patterns (Python cache files, etc.)
├── .python-version         # Python version specification for pyenv
├── README.md               # This file - project documentation
├── CONTRIBUTING.md         # Guidelines for contributing to this project
├── LICENSE                 # MIT License for this project
├── requirements.txt        # Python dependencies (currently none)
├── hello_world.py          # Main program file
└── test_hello_world.py     # Unit tests for the program
```

## Learning Points

### Code Structure
The program follows Python best practices:
- **Shebang line**: `#!/usr/bin/env python3` enables direct execution on Unix systems
- **Module docstring**: Explains what the program does and how to use it
- **Constants**: `GREETING_MESSAGE` is a constant that could easily be changed
- **Function separation**: Logic is in `main()` function for better organization
- **Main guard**: `if __name__ == "__main__":` ensures code runs only when executed directly

### Why Use a Function for Something So Simple?
Even though our program just prints one line, putting it in a `main()` function demonstrates good habits:
- The function can be imported and called from other modules
- It can be tested programmatically (see `test_hello_world.py`)
- It's easier to extend with more functionality later
- It follows the pattern used in real-world projects

### The Main Guard Pattern
The `if __name__ == "__main__":` pattern is important because:
- It prevents code from running when the module is imported
- It makes the module reusable in other programs
- It's a standard Python idiom you'll see everywhere
- It enables proper testing of the module

## Development

This project follows Python best practices:
- **PEP 8 style guidelines**: Official Python code style
- **Clean project structure**: Organized and easy to navigate
- **Proper version control**: Uses Git for tracking changes
- **Cross-platform compatibility**: Works on Windows, macOS, and Linux
- **Comprehensive documentation**: Clear instructions and explanations
- **Test coverage**: Includes unit tests for verification

### Code Style
This project adheres to PEP 8, Python's official style guide. You can check code style with:

```bash
# Install flake8 if needed
pip install flake8

# Check code style
flake8 hello_world.py
```

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

This is an educational demonstration project created to teach Python fundamentals and professional development practices.

## Additional Resources

Want to learn more? Check out these resources:
- [Python Official Documentation](https://docs.python.org/3/)
- [PEP 8 - Style Guide for Python Code](https://pep8.org/)
- [Python Testing with unittest](https://docs.python.org/3/library/unittest.html)
- [Real Python Tutorials](https://realpython.com/)

---

**Happy Learning!** This project demonstrates that even simple programs deserve clean code, good structure, and thorough documentation.
