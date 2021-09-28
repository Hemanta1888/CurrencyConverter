# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 03:23:18 2021

@author: Hemanta
"""

print("Welcome to the currency converter")
USD = 73.475
NZD = 51.5209
EURO = 86.635
AUD = 53.725
YEN = 0.669
while True:
    que = input("Do you want to exchange your currency[yes/no] ")
    if que == 'yes':
        print("Thank you for showing your interest to change currency")
        print("1. Convert (INR to USD/USD to INR)")
        print("2. Convert (INR to NZD/NZD to INR)")
        print("3. Convert (INR to EURO/EURO to INR)")
        print("4. Convert (INR to AUD/AUD to INR)")
        print("5. Convert (INR to YEN/YEN to INR)")
        ans = int(input("Choose the currency to exchange: "))
        while True:
            if ans == 1:
                ask1 = input("what do you want to convert?[INR TO USD/ USD TO INR] ")
                if ask1 == 'INR TO USD':
                    ask = int(input("Enter the amount: "))
                    print("Convert INR to USD:",ask / USD)
                    print("Thank you for choosing our service")
                elif ask1 == 'USD TO INR':
                    ask = int(input("Enter the amount: "))
                    print("Convert INR to USD:",ask * USD)
                    print("Thank you for choosing our service")
                else:
                    print("Sorry! I didn't get it")
                break
            elif ans == 2:
                ask1 = input("what do you want to convert?[INR TO NZD/NZD TO INR] ")
                if ask1 == 'INR TO NZD':
                    ask = int(input("Enter the amount: "))
                    print("Convert INR to NZD:",ask / NZD)
                    print("Thank you for choosing our service")
                elif ask1 == 'NZD TO INR':
                    ask = int(input("Enter the amount: "))
                    print("Convert NZD to INR:",ask * NZD)
                    print("Thank you for choosing our service")
                else:
                    print("Sorry! I didn't get it")
                break
            elif ans == 3:
                ask1 = input("what do you want to convert?[INR TO EURO/EURO TO INR] ")
                if ask1 == 'INR TO EURO':
                    ask = int(input("Enter the amount: "))
                    print("Convert INR to EURO:",ask / EURO)
                    print("Thank you for choosing our service")
                elif ask1 == 'EURO TO INR':
                    ask = int(input("Enter the amount: "))
                    print("Convert EURO to INR:",ask * EURO)
                    print("Thank you for choosing our service")
                else:
                    print("Sorry! I didn't get it")
                break
            elif ans == 4:
                ask1 = input("what do you want to convert?[INR TO AUD/AUD TO INR] ")
                if ask1 == 'INR TO AUD':
                    ask = int(input("Enter the amount: "))
                    print("Convert INR to AUD:",ask / AUD)
                    print("Thank you for choosing our service")
                elif ask1 == 'AUD TO INR':
                    ask = int(input("Enter the amount: "))
                    print("Convert AUD to INR:",ask * AUD)
                    print("Thank you for choosing our service")
                else:
                    print("Sorry! I didn't get it")
                break           
            elif ans == 5:
                ask1 = input("what do you want to convert?[INR TO YEN/YEN TO INR] ")
                if ask1 == 'INR TO YEN':
                    ask = int(input("Enter the amount: "))
                    print("Convert INR to YEN:",ask / YEN)
                    print("Thank you for choosing our service")
                elif ask1 == 'YEN TO INR':
                    ask = int(input("Enter the amount: "))
                    print("Convert YEN to INR:",ask * YEN)
                    print("Thank you for choosing our service")
                else:
                    print("Sorry! I didn't get it")
                break
       
    elif que == 'no':
        print("Thank you for your response.")
        break