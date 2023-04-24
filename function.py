#drug wars clone by K9BFF
#functions

import math
import random
import var

global totalPrice
global cash
global debt

# $60 for a gram? thats a steal!
def prices():
    global weedPrice
    weedPrice = random.randint(10,60)
    print("Current PRICES are:")
    print("WEED:", weedPrice)

# time to choose... its time to choose
def choice():
    print("Will you (B)uy, (S)ell, or (J)et?")
    choice = input("# ").lower()
    if choice == "b":
        print("How many?")
        bAmount = int(input("# "))
        totalPrice = (weedPrice * bAmount)
        var.cash = (var.cash - totalPrice)

    elif choice == "s":
        print("How many?")
        sAmount = int(input("# "))
        salePrice = (weedPrice * sAmount)
        var.cash = (var.cash + salePrice)