# sphere.py - Lab 2
# 
# Name: Daeshaun Morrison
# Date: 9/1/2020
#
# Given the radius of a sphere, this program computes its 
# diameter, surface area, and volume.

# A useful value:
PI = 3.14159265359

# Initialize the radius:r
radius = float(input("What is the sphere's radius? :"))

# Calculate the properties of the sphere:

diameter = radius * 2
surfaceArea = 4 * PI * radius**2
volume = (4/3) * PI * radius**3

# Print the results:
print(f" sphere radius = {radius}\n \n diameter = {diameter} \n area     = {surfaceArea} \n volume   = {volume}")


