"""
CP1404/CP5632 Practical
Subject reader - reads subject data from a file
"""

FILENAME = "subject_data.txt"


def main():
    data = get_subject_data(FILENAME)
    display_subjects(data)


def get_subject_data(filename):
    """Read subject data from file and return as list of tuples."""
    subject_data = []
    with open(filename, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            subject = parts[0]
            students = int(parts[1])
            instructor = parts[2]
            subject_data.append((subject, students, instructor))
    return subject_data


def display_subjects(data):
    """Display subject data in formatted form."""
    for subject, students, instructor in data:
        print(f"{subject} is taught by {instructor} and has {students} students")


main()
