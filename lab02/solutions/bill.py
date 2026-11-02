# bill.py -- solution to D2
# Split a restaurant bill, including the tip, between a number of people.
# Known crashes (fix them after session 3): 0 people -> ZeroDivisionError,
# text instead of a number -> ValueError.

total = float(input("Total bill (EUR): "))
people = int(input("Number of people: "))
tip_percent = float(input("Tip in percent: "))

with_tip = total * (1 + tip_percent / 100)
per_person = with_tip / people
print("Each person pays:", round(per_person, 2), "EUR")
