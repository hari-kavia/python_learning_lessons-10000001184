# PUBLIC_INTERFACE
def counter():
    """Return a closure that increments and remembers its own count."""
    count = 0

    # PUBLIC_INTERFACE
    def increment():
        """Increase the captured count by one and return its new value."""
        nonlocal count
        count += 1
        return count

    return increment


if __name__ == "__main__":
    first_counter = counter()
    second_counter = counter()

    print(first_counter())   # 1
    print(first_counter())   # 2: the closure remembers the previous count.
    print(second_counter())  # 1: each closure has its own count.
    print(first_counter())   # 3: the first closure keeps its own state.
