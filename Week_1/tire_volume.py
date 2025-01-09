"""
==========================================
    Program: Tire Volume
    Author: Arthur Weale
    Date: 1-08-2025
    Description:
        The script measures the tire volume and rights the data in a text file.
==========================================
"""
#Imports the math function
import math

#Imports the datetime finction
from datetime import datetime

#Declared Variables
tire_width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
tire_diameter = int(input("Enter the diameter os the wheel in inches (ex 15): "))
pie = math.pi
today = datetime.now()

#Calculates tire volume
def calculate_tire_volume ():
    tire_volume = ((pie * tire_width ** 2 * aspect_ratio) * (tire_width * aspect_ratio + 2540 * tire_diameter))/10000000000
    print(f'The approximate volume is {tire_volume:.2f} litres')
    return tire_volume

calculate_tire_volume()

buy_tires = input(f"Would you like to buy the 4 tires type {tire_width}/{aspect_ratio}-{tire_diameter}: ")

#Reinitislise the phone number
phone_number = ""

if buy_tires.lower() == "yes":
    phone_number = input("Please input your phone number: ")
    
    while len(phone_number) != 10:
        print("Your phone number is not either exceeds the number of digits or is not enough")
        phone_number = input("Please input your phone number: ")
        print("Thank you for the purchase, the receipt will be sent to you message inbox.")
elif buy_tires.lower() == "no":
    print("Thank you")

#Writing in text file
with open("volumes.txt","at") as volumes_file:
    print(f"{today : %Y-%m-%d}, {tire_width}, {aspect_ratio}, {tire_diameter}, {phone_number}", file=volumes_file)
    print("Data successfully written to volumes.txt.")  # Confirmation message