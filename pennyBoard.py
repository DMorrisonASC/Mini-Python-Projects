# pennyBoard.py - Lab 5
# Author: Daeshaun Morrison
# Date: 9/22/2020
# purpose: To  calcualate exactly how much 
# a friend will pay when they pay for each square of a checkers
# board. The catch is if the friend puts 
# a single penny (1¢) on the first square of the 
# checkerboard, and then puts double that (2¢) on the second square, and 
# then puts double yet again (4¢) on the third square, doubling it again (8¢) on 
# the fourth square, etc…


moneyToPay = 1
totalPennies = 1
print(f"Square  Number of pennies\n------  -----------------")
for item in range(1, 64+1):
    print(f"{item}       {moneyToPay:,}")
    moneyToPay = moneyToPay * 2
    totalPennies = totalPennies + moneyToPay
# Calcualate how many dollars are there($1 = 100¢)
# Round down because cents is the lowest amount
totalInDollar = totalPennies // 100
penniesLeft = totalPennies % 100
# Get weight of all the pennies in grams then convert to pounds
# penny weighs 2.5 g, and 1 pound is equivalent to 453.6 g).
penniesToGram = totalPennies * 2.5
penniesToPounds = penniesToGram // 435.6
# Calcualate the cost of making those pennies, $3.15 per pound
costOfPennies = penniesToPounds * 3.15
print(f"Summary\n---------------")
print(f"To pay for 64 squares, you'll need ${totalInDollar:,}.{penniesLeft}¢!")
print(f"All those pennies weight approximately {penniesToPounds:,} pounds")
print(f"It cost {costOfPennies:,} to make all those pennies")




    
    