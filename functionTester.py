# functionTester.py
# A program for testing the use of some iterative functions that calculate
# solutions to some simple mathematical problems.
#
# Name: Daeshaun Morrison
# Date: 9/29/2020
#

def main() :

    ## DO NOT MODIFY main()
    
    # Get two non-negative integers from the user less than the specified max 
    print("Enter a value for n(0-100):")
    num = getIntFromUser(100)
    print()
    print("Enter a value for p(0-20):")
    power = getIntFromUser(20)
    
    # Calculate various interesting things
    summ = summation(num)
    fact = factorial(num)
    expntl = exponential(num, power)
    fibonacciNum = fibonacci(num)
    
    # Provide some nicely formatted output
    printResults(num, power, summ, fact, expntl, fibonacciNum)

    

# getIntFromUser:
# This function will prompt the user for an integer between 0 and maxNum,
# and will re-prompt as necessary until a valid input is received.
def getIntFromUser(maxNum):
    
    # Check if input is valid, if not keep asking for one
    while True:
        try:
            inputNum = int(input())
        except Exception:
            print(f"Please use a number from 0 to {maxNum}: ")
            continue

        if (inputNum >= 0 and inputNum <= maxNum) :
            break
        else:
            print(f"Please use a number from 0 to {maxNum}: ")
            continue
    return inputNum

# Summation:
def summation(n) :
    #  The addition of a sequence of any kind of numbers, called addends or summands; the result is their sum or total.
    total = 0
    for i in range(0, n+1):
        total = total + i
    return total

# Factorial:
def factorial(n):
    # The product of an integer and all the integers below it; e.g. factorial four ( 4! ) is equal to 24(1 * 2 * 3 * 4).
    factorialNum = 1
    for item in range( 1 , n + 1):
        factorialNum = factorialNum * item  
    return factorialNum  

# Exponential:
def exponential(n, p):
    # This proforms the Exponential - operation of raising one quantity to the power of another.
    exponNum = n
    for item in range(0, p-1):
        exponNum = exponNum * p
    return exponNum
def fibonacci(n):
    # fibonacci first 2 number are ([0, 1]) by default
    # The next number is found by adding up the two numbers before it:
    # the 2 is found by adding the two numbers before it (1+1),
    # the 3 is found by adding the two numbers before it (1+2),
    # the 5 is (2+3),
    # and so on! 
    fibonacciList = [0, 1]
    if n == 0:
        n = [0]
    elif n == 1:
        n == [0, 1]
    else:
        for item in range(2, n+1):
            fib = fibonacciList[item-1 ] + fibonacciList[item-2]
            fibonacciList.append(fib)
    return fibonacciList
# printResults:
def printResults(n, p, s, f, e, fib):
    # This function has no return value. It takes several input arguments which represent the
    # input values and the results calculated by the other functions. 
    print(f"""Function Tester\
\n  Inputs:\
\n  n = {n}\
\n  p = {p}\
\nResults:\
\n  Summation({n}) = {s:,}\
\n  Factorial({n}) = {f:,}\
\n  Exponential: {n}^{p} = {e:,}\
\n  Fibonacci: {fib}\
""")
    

# Start the program running
main()   # This must be the last line in the file
