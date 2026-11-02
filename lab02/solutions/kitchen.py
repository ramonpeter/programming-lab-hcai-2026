# kitchen.py -- solution to D4
FLOUR_G_PER_CUP = 125
SUGAR_G_PER_CUP = 200

grams = float(input("Grams: "))
print("Flour:", round(grams / FLOUR_G_PER_CUP, 2), "cups")
print("Sugar:", round(grams / SUGAR_G_PER_CUP, 2), "cups")
