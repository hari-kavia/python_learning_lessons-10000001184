"""Example: pack and unpack a tuple containing a student's scores."""


if __name__ == '__main__':
    # Comma-separated values are packed into a tuple.
    student = ('Maya', 85, 90, 95)
    print(f"Student record: {student}")

    # A starred target collects the remaining values into a list.
    name, *scores = student
    print(f"Name: {name}")
    print(f"Scores: {scores}")
    print(f"Average score: {sum(scores) / len(scores):.1f}")

    # Unpacking can also select the first and last values.
    first_score, *middle_scores, last_score = scores
    print(f"First and last scores: {first_score}, {last_score}")

    # The trailing comma makes this a tuple rather than a string.
    single_student = (name,)
    print(f"Single-item tuple: {single_student}")
