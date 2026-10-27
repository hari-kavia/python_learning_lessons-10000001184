"""Example: log a function call without changing its return value."""

from functools import wraps


# PUBLIC_INTERFACE
def log_call(original_function):
    """Decorate a function to print its name and result when called."""
    @wraps(original_function)
    def wrapper(*args, **kwargs):
        """Forward all arguments and return the original function's result."""
        print(f"Calling {original_function.__name__}")
        result = original_function(*args, **kwargs)
        print(f"Result: {result}")
        return result

    return wrapper


# PUBLIC_INTERFACE
@log_call
def add(first, second):
    """Return the sum of two numbers."""
    return first + second


if __name__ == '__main__':
    # The wrapper accepts both positional and keyword arguments.
    total = add(3, second=4)
    print(f"Returned value: {total}")
    # wraps preserves the original function's name and docstring.
    print(f"Function name: {add.__name__}")
