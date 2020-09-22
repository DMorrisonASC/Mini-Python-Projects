# oddEven.py - Lab 5
# Author: Daeshaun Morrison
# Date: 9/21/2020
# purpose: To tell user if a number is even or odd

# Get user's input
numInput = input("Put a number, it'll tell you if it's odd or even: ")

# Set while loop that will continue asking the user 
# for a number until they quit by typing a word that
# starts with a "Q"(including lower case) 
while True :
    # First, check if it's a "Q". If so,
    # print a good bye message and
    # end program
    if numInput.lower().startswith("q") :
        print(f"Thanks for using us, see you later!")
        break
    # If number has no reminder when divided by 2
    # tell user it's an even number
    elif float(numInput) % 2 == 0 :
        print(f"It's an even number!")
    # If it has a reminder, tell them it's odd.
    elif not float(numInput) % 2 == 0:
        print(f"It's an odd number!")
    else: 
        print("That's not a number!")
    
    numInput = input("Try another number: ")




    
