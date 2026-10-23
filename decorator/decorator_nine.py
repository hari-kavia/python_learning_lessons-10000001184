"""Beginner example: add behavior to a function without changing its body.

Run with: python decorator/decorator_nine.py
"""


# PUBLIC_INTERFACE
def simple_decorator(original_function):
    """Wrap a no-argument function with messages before and after its call."""
    def wrapper():
        """Call the original function and keep its return value."""
        print("Before the greeting")
        result = original_function()
        print("After the greeting")
        return result

    # Return the wrapper itself, not wrapper(), so it can be called later.
    return wrapper


# PUBLIC_INTERFACE
@simple_decorator
def say_hello():
    """Print a friendly greeting."""
    print("Hello, Python learner!")


# @simple_decorator is shorthand for say_hello = simple_decorator(say_hello).
# The main guard runs the example only when this file is executed directly.
if __name__ == "__main__":
    say_hello()

# Expected output:
# Before the greeting
# Hello, Python learner!
# After the greeting
