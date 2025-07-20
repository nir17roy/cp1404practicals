"""CP1404/CP5632 Practical
Read programming language data from file and display as objects.
"""

from programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details, save as objects, display."""
    languages = load_languages("languages.csv")
    display_languages(languages)


def load_languages(filename):
    """Load languages from a CSV file and return a list of ProgrammingLanguage objects."""
    languages = []
    with open(filename, 'r') as in_file:
        next(in_file)  # Skip header
        for line in in_file:
            parts = line.strip().split(',')
            name = parts[0]
            typing = parts[1]
            reflection = parts[2] == "Yes"
            year = int(parts[3])
            language = ProgrammingLanguage(name, typing, reflection, year)
            languages.append(language)
    return languages


def display_languages(languages):
    """Print each language using its __repr__ format."""
    for language in languages:
        print(language)


if __name__ == "__main__":
    main()
