"""CP1404/CP5632 Practical - Client code to use the ProgrammingLanguage class."""

from programming_language import ProgrammingLanguage


def main():
    """Test ProgrammingLanguage class and filter dynamic languages."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]

    print("All languages:")
    for language in languages:
        print(language)

    print("\nDynamically typed languages:")
    for language in languages:
        if language.is_dynamic():
            print(language)


main()
