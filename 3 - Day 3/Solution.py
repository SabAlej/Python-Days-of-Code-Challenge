# Write a function to count the number of vowels in a given string 
# (a, e, i, o, u).

def count_vowels(string):
    vowels = 0
    for char in string:
        if char in "aeiou":
            vowels += 1
    return vowels

print('The word Hello has',count_vowels("hello"),'vowels.')

print('The word World has',count_vowels("world"),'vowels.')



