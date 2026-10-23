"""A beginner example of basic Python dictionary operations."""


# PUBLIC_INTERFACE
def main():
    """Demonstrate dictionary operations using a simple student record."""
    # A dictionary stores information as key-value pairs.
    student = {"name": "Alex", "age": 18}
    print("Original dictionary:", student)

    # Read a value using its key.
    print("Student name:", student["name"])

    # Add a new key-value pair.
    student["subject"] = "Python"
    print("After adding a subject:", student)

    # Update the value of an existing key.
    student["age"] = 19
    print("After updating the age:", student)

    # Use get() to safely look up a key that might not exist.
    print("Grade:", student.get("grade", "Not assigned"))

    # Remove a key-value pair.
    del student["subject"]
    print("After removing the subject:", student)

    # Loop through all remaining keys and values.
    print("Student details:")
    for key, value in student.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
