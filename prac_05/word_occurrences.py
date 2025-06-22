"""
CP1404/CP5632 Practical
Word occurrences in a string
"""

def main():
    text = input("Text: ")
    words = text.split()
    word_to_count = {}
    for word in words:
        word_to_count[word] = word_to_count.get(word, 0) + 1

    for word, count in sorted(word_to_count.items()):
        print(f"{word:<10} : {count}")


main()
