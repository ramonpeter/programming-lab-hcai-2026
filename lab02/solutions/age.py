# age.py -- solution to D1
# int(...) turns the text the user typed into a whole number.
# Typing "twenty" still crashes, with a ValueError: handling that is session 3 (try / except).

age = int(input("How old are you? "))
print("Next year you will be", age + 1)
