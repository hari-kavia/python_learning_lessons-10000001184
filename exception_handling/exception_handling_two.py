"""Demonstrate try/except/else/finally with numeric input and division."""


# PUBLIC_INTERFACE
def divide_numbers(numerator: str, denominator: str):
    """Convert two numeric strings and return their quotient, or None on error.

    ValueError handles invalid numeric text; ZeroDivisionError handles a zero
    denominator. The finally block runs whether division succeeds or fails.
    """
    try:
        result = float(numerator) / float(denominator)
    except ValueError:
        print("Invalid input: both values must be numbers.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        # This branch runs only when the try block completes without an error.
        print(f"Result: {result}")
        return result
    finally:
        print("Division attempt finished.")

    return None


# PUBLIC_INTERFACE
def main():
    """Run successful, invalid-input, and zero-denominator examples."""
    for numerator, denominator in [("10", "2"), ("ten", "2"), ("10", "0")]:
        print(f"\nDividing {numerator} by {denominator}:")
        divide_numbers(numerator, denominator)


if __name__ == "__main__":
    main()
