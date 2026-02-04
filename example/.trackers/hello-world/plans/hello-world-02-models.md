# Phase 2: Models - hello-world

**Phase Number**: 2
**Status**: Pending
**Dependencies**: Phase 1 (Foundational)

## Phase Overview

This phase defines the data structures and constants needed for the Hello World program. In this simple project, "models" refers to configuration constants rather than complex data classes.

This phase includes tasks for the following tracks:
- **hello-world**: Define the greeting message constant

## Implementation Context

Building on the foundational setup from Phase 1, this phase establishes the data layer for our Hello World program. While a typical application would include entity classes, DTOs, and value objects, our simple program only requires a message constant.

**Key Patterns**:
- Follow PEP 8 constant naming conventions (UPPER_CASE)
- Separate configuration from logic
- Make constants easily modifiable
- Document the purpose of each constant

**Important Considerations**:
- Keep it simple - just define what's needed
- Make the constant reusable for potential future enhancements
- Follow Python naming conventions
- Add clear documentation for educational purposes

---

## Track: hello-world

### Task 1: Define message constants

**Complexity**: 1 (Low)
**Track**: hello-world
**Status**: Pending
**Estimated Effort**: Small (10 minutes)

#### Description

Create configuration constants for the greeting message that will be displayed by the program. This demonstrates the principle of separating data/configuration from business logic, even in a simple program.

By defining the message as a constant rather than hardcoding it in the print statement, we make the code more maintainable and easier to customize. This is an important pattern that scales to larger applications.

#### Acceptance Criteria

- [ ] Constant `GREETING_MESSAGE` is defined
- [ ] Constant value is exactly "Hello, World!"
- [ ] Constant has clear docstring or comment
- [ ] Constant follows PEP 8 naming style (UPPER_CASE)
- [ ] Constant is easily modifiable for future customization

#### Implementation Details

Define the greeting message constant at the module level of the main program file.

**Files to Create/Modify**:
- `hello_world.py` - Add constant definition at the top of the file

**Key Considerations**:
- Place constant after module docstring but before function definitions
- Use all uppercase for constant name (PEP 8 convention)
- Add a comment explaining the constant's purpose
- Keep the value simple: exactly "Hello, World!"

**Implementation Steps**:
1. In `hello_world.py`, add constant after the module docstring:
   ```python
   # Constants
   GREETING_MESSAGE = "Hello, World!"
   ```
2. Add a brief comment explaining the constant:
   ```python
   # Constants
   GREETING_MESSAGE = "Hello, World!"  # The message to display to the user
   ```
3. Ensure proper spacing around the constant (blank lines before and after the constants section)

**Pattern Example**:
```python
#!/usr/bin/env python3
"""
Module docstring here
"""

# Constants
GREETING_MESSAGE = "Hello, World!"  # The greeting message to display


def main():
    """Main function"""
    # Will use GREETING_MESSAGE here
    pass
```

**Dependencies**:
- Task 1.1 (Project structure)
- Task 1.2 (Python environment)

**Testing**:
- Verify constant is accessible from within the module
- Verify constant value is correct: `"Hello, World!"`
- Run linter (flake8/pylint) to verify PEP 8 compliance
- Confirm constant naming follows convention

---

## Phase Completion Checklist

After completing all tasks in this phase, verify:

- [ ] All tasks in this phase are implemented
- [ ] Constant follows PEP 8 naming conventions
- [ ] Constant has appropriate documentation
- [ ] Constant is easily accessible for use in main program
- [ ] Code follows project patterns and conventions
- [ ] Linter shows no warnings for the constant definition
- [ ] Ready to proceed to Phase 3 (or skip to Phase 7 for this project)

## Notes

**Separation of Concerns**:
Even in a simple program, separating configuration (the message) from logic (the printing) is good practice. This makes the code more maintainable and demonstrates a principle that's crucial in larger applications.

**Educational Value**:
This phase teaches:
- Python constant naming conventions
- Why constants are better than magic strings
- Module-level organization
- Separation of data and logic

**Future Extensibility**:
With the message as a constant, it's easy to:
- Change the greeting message
- Add multiple message variants
- Load messages from configuration files
- Support internationalization (i18n)

**Why Not a Class?**:
For this simple program, a constant is sufficient. In a larger application, we might create a `Config` class or use a configuration management library, but that would be over-engineering for Hello World.
