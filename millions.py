# millions.py - Lab 3 
# Author: Daeshaun Morrison
# Date: 9/8/2020
# purpose: Create a list of the odd integers from 0 to 10,000,000

# Get list of all numbers from 0 to 10,000,000(10 million)
# The 1st param of `range` is the starting number(0)
# The 2nd param of `range` is the ending number(10000000)
# The 3rd param of `range` is the number it is counting by (3)
listOddNums = list( range( 0, 10000000, 3) )
# It count from 0 to 10 million by 3s -> 0...3...6...9....
print(f"The min number is {min(listOddNums)}\nThe max number is {max(listOddNums)}")
print(f"There are {len(listOddNums)} odd numbers in 10 million")
print(f"The total(sum of all numbers) is {sum(listOddNums)}")
print(f"The average(sum/lenght) is {sum(listOddNums)/len(listOddNums)}")


