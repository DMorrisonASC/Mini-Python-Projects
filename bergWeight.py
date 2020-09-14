# bergWeight.py - Lab 3 
# Author: Daeshaun Morrison
# Date: 9/8/2020
# purpose: To calcuate the weight in pounds and ounces of a monthly production

# Cool start screen :)
print(f"==============================\nPounds Of Berg Bars Per Month!\n==============================")
# Ask the user for the weight of a single Berg Bar (a floating-point number)
weightBergBar = float(input(f"What is the weight of a single Berg Bar in ounces?"))

# Ask for number of Berg Bars made that month (an integer).
monthlyBergBars = int(input(f"How many are made monthly?"))

# Calculate the total weight of that month’s production in ounces.
weightOfBarsMonthly = float(weightBergBar * monthlyBergBars)
# Set constant for how many ounces are in a pound
ouncesInPound = int(16)
# Find pounds and ounces per mounthly production
poundsPerMonth = round((weightOfBarsMonthly / ouncesInPound), 2)
leftoverOunces = round((weightOfBarsMonthly % ouncesInPound), 2)

# Extra Credit - Convert ounces to grams

# Set constant for how many grams are in an ounce
gramsPerOunce = 28.35
ouncesToGrams = round((weightOfBarsMonthly * gramsPerOunce), 2)
# Set constant for how many grams are in a kilogram
gramsPerKilograms = 1000
# 1000 grams in a kilogram -> grams / 1000 = kilograms
gramsToKilograms = round((ouncesToGrams / gramsPerKilograms), 2)
leftoverGrams = round((ouncesToGrams % gramsPerKilograms), 2)
print(f"==============================")
print(f"Weight of each Berg Bar: {weightBergBar}\nBergbars produced monthly: {monthlyBergBars}")
print(f"The total weight produced is about {poundsPerMonth:,} pounds and {leftoverOunces:,} ounces")
print(f"Silly Americans, convert to metric!")
print(f"The total weight produced is {gramsToKilograms:,} kilograms and {leftoverGrams:,} grams!")

