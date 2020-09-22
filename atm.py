# atm.py - Lab 5
# Author: Daeshaun Morrison
# Date: 9/22/2020
# purpose: To simulate an ATM machine by 
# allowing user to deposit, withdraw and 
# check their account balances

print(f"""Welcome to Kicking Mule Bank\nAvailable actions:\
\n      (B)alance inquiry\
\n      (D)eposit\
\n      (W)ithdrawal\
\n      (Q)uit""")
# Ask for user input
actions = input(f"Please make a selection: ")
keepGoing = True
# Set the balance at zero 
balance = float(0)
# Run function until keepGoing is changed to "False"
while keepGoing :
    # If user doesn't enter a 
    # valid input("q", "b", "d", "w"),
    # keep asking to enter correct one.
    # If correct, continue to program
    while True :
        if actions.lower().startswith("q") :
            break
        elif actions.lower().startswith("b"):
            break
        elif actions.lower().startswith("d"):
            break
        elif actions.lower().startswith("w"):
            break    
        else:
            actions = input(f"Invaild selection, try again: ")
            continue
    # If user types a word that starts with "q"
    # end program.
    if actions.lower().startswith("q") :
        keepGoing = False
        print(f"You successful exited the ATM!")
    
    # if "b" check balance
    elif actions.lower().startswith("b") :
        print(f"Your current balance is ${balance:,.2f}¢")
    
    # if "d" ask how much to deposit 
    elif actions.lower().startswith("d") :
        # check and make sure it's a valid input
        # if not, keep asking for one.
        try:
            deposit = float(input(f"How much do you want to deposit?: "))
        except Exception:
            print(f"Put a valid input")
            continue
        # If deposit is more than 0, add to balance.
        # else keep asking.
        if deposit > 0 :
            balance = balance + deposit
        else:
            print(f"Amount needs to greater than $0")
            continue
    # if "w" withdraw money
    elif actions.lower().startswith("w") :
        # check and make sure it's a valid input
        # if not, keep asking for one.        
        try:
            withdrawal = float(input(f"How much do you want to withdraw?: "))
        except Exception:
            print(f"Put a valid input")
            continue
        # Make sure they can't withdraw more money than
        # what is in their account.
        if (withdrawal > balance):
            print(f"You can't withdraw more than your balance")
            continue
        # Prevent withdrawing of negative numbers
        elif (withdrawal <= 0):
            print(f"You can't withdraw negative amount")
            continue
        else: 
            balance = balance - withdrawal
    # After action is done, ask if they want to continue.
    # ends programs if "q" is typed
    actions = input(f"Please make a selection: ")
     
