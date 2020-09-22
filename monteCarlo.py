# monteCarlo.py - Lab 4
# Author: Daeshaun Morrison
# Date: 9/16/2020
# purpose: # To Get an estimate of Pie using this equation
# 𝜋 = 4 × (hits/shots). It represents the ratio of "shots" that hit the circle's area in a square.

# Import the Random() library 
from random import random
# Prompt the user for the number of trials
trialsNum = int(input(f"How many trials do you want to run?(Ex. 100,000): "))
# set X & Y coordinate the shots
x = 0
y = 0
# set `shots` & `hits` to 0
shots = 0
hits = 0
# Runs the loops as many times as user input(ex. 100,000x)
for num in range(trialsNum):
    # record each shot
    shots = shots + 1
    x = (2 * random() ) - 1.0
    y = (2 * random() ) - 1.0
    # record each hit if it's in the circle's area    
    if ((x ** 2) + (y ** 2) <= 1) :
        hits = hits + 1
    # Get an estimate of Pie using this equation
    # 𝜋 = 4 × (hits/shots)
    PieEstimate = 4 * (hits/shots)

print(PieEstimate)