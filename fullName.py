# fullName.py - Lab2
# Author: Daeshaun Morrison
# Date: 9/1/2020

# If "continueNaming" = true, it keeps asking user to input their name.
# If false, program stops

continueNaming = True
# While continueNaming is true...ran the program
while continueNaming :
        
    #User inputs their first & last name
    firstName = input("What's your first name?")
    lastName = input("What's your last name(s)?")   
    # logs it
    print(f"{lastName}, {firstName}")

    # Ask if they want to continue
    while True:
        noOrYes = input(f"Do you want to continue? (Y/N)")
        if noOrYes.lower().startswith('y'):
            #User gave a proper response
            #we're ready to exit the loop.
            break
        elif noOrYes.lower().startswith('n'):
            #User gave a proper response,
            #we're ready to exit the loop.
            break
        else: 
            print("Sorry, I didn't understand that.")
            #Better try again... returning to the start of the loop
            continue
        
    # If yes or any other programmed equivalent, "continueNaming = True",
    # which contines the program
    if noOrYes.lower().startswith('y'):
            continueNaming = True
            
    # If no or any other programmed equivalent, "continueNaming = false",
    # ending the program   
    elif noOrYes.lower().startswith('n'):
        continueNaming = False
            
