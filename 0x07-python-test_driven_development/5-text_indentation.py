#!/usr/bin/python3
"""Module prints two new lines after '.', '?', ':'

Example:

    >>> text_indentation("Love. Is. Kind.") # doctest: +NORMALIZE_WHITESPACE
    Love
    <BLANKLINE>
    Is
    <BLANKLINE>
    Kind
    <BLANKLINE>

"""


def text_indentation(text):
    """Prints two lines after either of these characters '.', '?', ':'

    Parameters:
        text (str): text to work on

    Return:
        void
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if (i != 0 and text[i - 1] in ['.', ':', '?']):
                continue
        if text[i] not in ['.', '?', ':']:
            print(text[i], end="")
        elif text[i] in ['.', '?', ':']:
            print("{}\n".format(text[i]))

            
