"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between.

    >>> repeat_string("hi", 1)
    'hi'
    >>> repeat_string("hi", 3)
    'hi hi hi'
    >>> repeat_string("x", 0)
    ''
    """
    if n <= 0:
        return ""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """Return True if the length of word is greater than or equal to length.

    >>> is_long_word("hello")
    True
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifragilisticexpialidocious", 10)
    True
    """
    return len(word) >= length


def format_sentence(phrase):
    """Format phrase as a sentence: capitalised and ending with a single full stop.

    >>> format_sentence('hello')
    'Hello.'
    >>> format_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_sentence('multiple spaces  here')
    'Multiple spaces  here.'
    """
    phrase = phrase.strip()
    if not phrase:
        return "."
    phrase = phrase[0].upper() + phrase[1:]
    if phrase.endswith("."):
        phrase = phrase.rstrip(".") + "."
    else:
        phrase += "."
    return phrase


if __name__ == "__main__":
    doctest.testmod()
