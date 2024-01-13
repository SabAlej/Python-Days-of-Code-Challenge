"""
This module contains a function to count the number of vowels in a given string.
"""

def count_vowels(string):
    """
    Count the number of vowels in a given string.

    Args:
        string (str): The string to count vowels in.

    Returns:
        int: The number of vowels in the string.
    """
    vowels = 0
    for char in string:
        if char in "aeiou":
            vowels += 1
    return vowels

print('The word Hello has',count_vowels("hello"),'vowels.')

print('The word World has',count_vowels("world"),'vowels.')
