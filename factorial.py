# factorial.py - Lab 5
# Author: Daeshaun Morrison
# Date: 9/21/2020
# purpose: To perform factorial on numbers.

# Get user's input
numInput = int(input(f"Enter an integer (negative to quit): "))

# Set & check a condition for the while loop 
while numInput >= 0 :
    # Set the value that will be multilpied continuously
    factorialNum = 1
    # If 0, default it to 0
    # Since in factorials, 0 always equals 1
    if numInput == 0 : 
        print(f"{numInput}! = 1")
    else:
        # Run a loop that does factorials
        for item in range( 1 , numInput + 1):
            factorialNum = factorialNum * item
        print(f"{numInput}! = {factorialNum:,}")
    # Ask user again for an input and keep asking running until the input is negative.
    numInput = int(input(f"Enter an integer (negative to quit): "))
print(f"Done!")