# listTools.py - Lab 3 
# Author: Daeshaun Morrison
# Date: 9/8/2020
# Purpose: Find the sum, average and the amount of elements in a list

myList = [10, -5, 14, 0, 47, -12, 17, -4]

count = 0
sumOfNums = 0
# The for loop keeps running code as long as the lenght of the list(myList)
# / until all elements are iterated
for num in myList:
    count = count + 1
    sumOfNums = num + sumOfNums

print(f" The list is {myList}\n\n Count   = {count}\n Sum     = {sumOfNums}")
print(f" Average = {sumOfNums/count}")   
