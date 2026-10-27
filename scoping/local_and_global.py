"""Example: look up the same variable name in different scopes."""

message = "global scope"


# PUBLIC_INTERFACE
def show_scopes():
    """Print local and enclosing values without changing the global value."""
    message = "enclosing scope"

    def show_local():
        """Create a local variable that shadows the enclosing variable."""
        message = "local scope"
        print(f"Inside show_local: {message}")

    def show_enclosing():
        """Read the enclosing variable because there is no local assignment."""
        print(f"Inside show_enclosing: {message}")

    show_local()
    show_enclosing()
    # The assignment in show_local does not change this enclosing variable.
    print(f"Inside show_scopes: {message}")


if __name__ == '__main__':
    show_scopes()
    # Neither function changes the module-level variable.
    print(f"Outside the functions: {message}")
