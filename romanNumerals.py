# romanNumerals.py - Lab 4
# Author: Daeshaun Morrison
# Date: 9/16/2020
# purpose: To convert any interger from 1-10 into a roman numeral. 

arabicNums = int(input(f"What number would you like to convert to a roman numeral?: "))

# Based on the value `arabicNums` matches, it prints a roman numeral of equivalency
if arabicNums == 1:
    print(f"{arabicNums} = I")
elif arabicNums == 2:
    print(f"{arabicNums} = II")
elif arabicNums == 3:
    print(f"{arabicNums} = III")
elif arabicNums == 4:
    print(f"{arabicNums} = IV")
elif arabicNums == 5:
    print(f"{arabicNums} = V")
elif arabicNums == 6:
    print(f"{arabicNums} = VI")
elif arabicNums == 7:
    print(f"{arabicNums} = VII")
elif arabicNums == 8:
    print(f"{arabicNums} = VIII")
elif arabicNums == 9:
    print(f"{arabicNums} = IX")
elif arabicNums == 10:
    print(f"{arabicNums} = X")
# If `arabicNums` is not between 1 to 10, tell user to use a number with range
else: 
    print(f"Use a number from 1 to 10!")




    
