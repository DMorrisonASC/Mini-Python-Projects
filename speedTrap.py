# speedTrap.py - Lab 4
# Author: Daeshaun Morrison
# Date: 9/16/2020
# purpose: To check if the user is driving at legal speed limit

# set a speed limit
legalSpeed = int(input(f"What's the local speed limit?: "))
# Input speed limit
speedTraveling = int(input(f"What speed are you going at?: "))
excessiveSpeeding = legalSpeed + 31

# Conditional that checks to see if legalSpeed vs. speedTraveling
# if legalSpeed is equal to or less than 25, inidicate that  the speed is legal
# if speedTraveling is 31 or more than the legalSpeed, then they will be charged with excessive speeding
# Otherwise, print a message indicating that the driver will receive a speeding ticket.
if speedTraveling <= legalSpeed :
    print(f"You were going at {speedTraveling} mpg, this is legal")
elif speedTraveling >= excessiveSpeeding:
    print(f"You were going at {speedTraveling} mpg, this is 31+ mpg above the speed limit. \nThis is a serious infraction. Your driver’s license suspensed for 15-days")
else:
    print(f"You were going at {speedTraveling}, this is above the speed limit. \nYou will be getting a speed ticket!")
  

    
