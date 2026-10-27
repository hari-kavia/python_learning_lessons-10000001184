"""Example: compare course enrollments using set differences."""


if __name__ == '__main__':
    # Converting a list to a set removes duplicate entries.
    python_students = set(['Adi', 'Tom', 'Maya', 'Tom'])
    java_students = {'Tom', 'Maya', 'Sara'}

    # Sets are unordered; sorting makes the printed results predictable.
    print(f"Python students: {sorted(python_students)}")

    # Difference contains students in the first set but not the second.
    print(f"Only Python: {sorted(python_students - java_students)}")
    print(f"Only Java: {sorted(java_students - python_students)}")

    # Symmetric difference contains students enrolled in exactly one course.
    print(f"Exactly one course: {sorted(python_students ^ java_students)}")
