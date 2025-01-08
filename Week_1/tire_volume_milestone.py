"""
==========================================
    Program: Tire Volume
    Author: Arthur Weale
    Date: 1-08-2025
    Description:
        A brief description of what the script does.
==========================================
"""
#Imports the math function
import math

#Declared Variables 
tire_width = int(input("Enter the width of the tire in mm: "))
aspect_ratio = int(input("Enter the aspect ratio of the tire: "))
tire_diameter = int(input("Enter the diameter os the wheel in inches: "))
pi = math.pi

#Calculates tire volume
tire_volume = ((pi * tire_width ** 2 * aspect_ratio) * (tire_width * aspect_ratio + 2540 * tire_diameter))/10000000000
print(f'The approximate volume is {tire_volume:.2f}')

