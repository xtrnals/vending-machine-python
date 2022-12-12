import time
print ("Welcome to Jasfer's Vending Machine!")
time.sleep(2)
# Creating variables for the items and their respective prices. 
drink_1 = "Coffee"
price_1 = 2.15
drink_2 = "Pepsi"
price_2 = 2.50
drink_3 = "Sprite"
price_3 = 1.75
drink_4 = "Gatorade"
price_4 = 2.35
drink_5 = "Iced Tea"
price_5 = 2.65
drink_6 = "Water"
price_6 = 0.75
snack_1 = "Doritos"
price_7 = 4.75
snack_2 = "Snickers"
price_8 = 3.45
snack_3 = "Oreos"
price_9 = 3.75
snack_4 = "Lays"
price_10 = 5
snack_5 = "Bounty"
price_11 = 4.25
snack_6 = "Salad Chips"
price_12 = 4.5
# Creating variables to track the number of each items bought,
coffee_bought = 0
pepsi_bought = 0
sprite_bought = 0
gatorade_bought = 0
iced_tea_bought = 0
water_bought = 0
doritos_bought = 0
snickers_bought = 0
oreos_bought = 0
lays_bought = 0
bounty_bought = 0
salad_chips_bought = 0
# Informing the user of the choices available and the prices that of each item.
print ("There are 6 drinks and 6 snacks available to pick from;\n")
time.sleep(2)
print (" Item                   Costs")
print (" ----                   -----")
print (" {}         ----->  {} ".format(drink_1, price_1))
print (" {}          ----->  {} ".format(drink_2, price_2))
print (" {}         ----->  {} ".format(drink_3, price_3))
print (" {}       ----->  {} ".format(drink_4, price_4))
print (" {}       ----->  {} ".format(drink_5, price_5))
print (" {}          ----->  {} ".format(drink_6, price_6))
print (" {}        ----->  {} ".format(snack_1, price_7))
print (" {}       ----->  {} ".format(snack_2, price_8))
print (" {}          ----->  {} ".format(snack_3, price_9))
print (" {}           ----->  {} ".format(snack_4,  price_10))
print (" {}         ----->  {} ".format(snack_5, price_11))
print (" {}    ----->  {} ".format(snack_6, price_12))
print ("")
# Asks the user how much money they would like to insert into the vending machine.
amount_of_10c = int(input("How many 10 cents coins would you like to insert? "))
while amount_of_10c < 0:
    amount_of_10c = int(input("Please enter a positive number."))
amount_of_25c = int(input("How many 25 cents coins would you like to insert? "))
while amount_of_25c < 0:
    amount_of_25c = int(input("Please enter a positive number."))
amount_of_50c = int(input("How many 50 cents coins would you like to insert? "))
while amount_of_50c < 0:
    amount_of_50c = int(input("Please enter a positive number."))
amount_of_1dollar = int(input("How many 1 dollar bills would you like to insert? "))
while amount_of_1dollar < 0:
    amount_of_1dollar = int(input("Please enter a positive number."))
# Creating a variable to store the total amount.
change = round(((amount_of_10c * 0.10) + (amount_of_25c * 0.25) + (amount_of_50c * 0.50) + (amount_of_1dollar * 1.00)),2)
# Informing the user how much they have entered in total.
print ("\nIn total you have entered $", change)
time.sleep(2)
# Asks the user to name the items they would wish to purchase and shows the remaining credit after each item.
while change > 0:
    customer_choice = input("Please enter the name of the item you want to purchase. Type N when you are finished \n")
    if customer_choice == "Coffee" or customer_choice == "coffee" and change >= price_1:
        print ("You have chosen a", drink_1, "these cost", price_1, "each,")
        print("Your drink is being dispersed...")
        time.sleep(2)
        change = round((change - price_1),2)
        coffee_bought = (coffee_bought + 1)
        print ("You have this much money remaining: $", change)
    elif customer_choice == "Pepsi" or customer_choice == "pepsi" and change >= price_2:
        print ("You have chosen a", drink_2, "these cost", price_2, "each,")
        print("Your drink is being dispersed...")
        time.sleep(2)
        change = round((change - price_2),2)
        pepsi_bought = (pepsi_bought + 1)
        print ("You have this much money remaining: $", change)
    elif customer_choice == "Sprite" or customer_choice == "sprite" and change >= price_3:
        print ("You have chosen a", drink_3, "these cost", price_3, "each,")
        print("Your drink is being dispersed...")
        time.sleep(2)
        change = round((change - price_3),2)
        sprite_bought = (sprite_bought + 1)
        print ("You have this much money remaining: $", change)
    elif customer_choice == "Gatorade" or customer_choice == "gatorade" and change >= price_4:
        print ("You have chosen a", drink_4, "these cost", price_4, "each,")
        print("Your drink is being dispersed...")
        time.sleep(2)
        change = round((change - price_4),2)
        gatorade_ways_bought = (gatorade_bought + 1)
        print ("You have this much money remaining: $", change)
    elif customer_choice == "Iced tea" or customer_choice == "iced tea" or customer_choice == "Iced Tea" and change >= price_5:
        print ("You have chosen a", drink_5, "these cost", price_5, "each,")
        print("Your drink is being dispersed...")
        time.sleep(2)
        change = round((change - price_5),2)
        iced_tea_bought = (iced_tea_bought + 1)
        print ("You have this much money remaining: $", change)
    elif customer_choice == "Water" or customer_choice == "water" and change >= price_6:
        print ("You have chosen a", drink_6, "these cost", price_6, "each,")
        print("Your drink is being dispersed...")
        time.sleep(2)
        change = round((change - price_6),2)
        water_bought = (water_bought + 1)
        print ("You have this much money remaining: $", change)
    elif customer_choice == "Doritos" or customer_choice == "doritos" and change >= price_7:
        print ("You have chosen a", snack_1, "these cost", price_7, "each,")
        print("Your snack is being dispersed...")
        time.sleep(2)
        change = round((change - price_7),2)
        doritos_bought = (doritos_bought + 1)
    elif customer_choice == "Snickers" or customer_choice == "snickers" and change >= price_8:
        print ("You have chosen a", snack_2, "these cost", price_8, "each,")
        print("Your snack is being dispersed...")
        time.sleep(2)
        change = round((change - price_8),2)
        snickers_bought = (snickers_bought + 1)
    elif customer_choice == "Oreos" or customer_choice == "oreos" and change >= price_9:
        print ("You have chosen a", snack_3, "these cost", price_9, "each,")
        print("Your snack is being dispersed...")
        time.sleep(2)
        change = round((change - price_9),2)
        oreos_bought = (oreos_bought + 1)
    elif customer_choice == "Lays" or customer_choice == "lays" and change >= price_10:
        print ("You have chosen a", snack_4, "these cost", price_10, "each,")
        print("Your snack is being dispersed...")
        time.sleep(2)
        change = round((change - price_10),2)
        lays_bought = (lays_bought + 1)
    elif customer_choice == "Bounty" or customer_choice == "bounty" and change >= price_11:
        print ("You have chosen a", snack_5, "these cost", price_11, "each,")
        print("Your snack is being dispersed...")
        time.sleep(2)
        change = round((change - price_11),2)
        bounty_bought = (bounty_bought + 1)
    elif customer_choice == "Salad Chips" or customer_choice == "salad chips" or customer_choice == "Salad chips" and change >= price_12:
        print ("You have chosen a", snack_6, "these cost", price_12, "each,")
        print("Your snack is being dispersed...")
        time.sleep(2)
        change = round((change - price_12),2)
        salad_chips_bought = (salad_chips_bought + 1)
        print ("You have this much money remaining: $", change)
    #When user inputs "N" or "n", their transaction will be done and the receipt is printed.
    elif customer_choice == "N" or customer_choice == "n":
        print ("\nThank you for using our vending machine!\n")
        time.sleep(2)
        print ("\nHere are your transaction details:\n")
        time.sleep(2)
        print ("You purchased: ")
        print (coffee_bought, "x", drink_1)
        print (pepsi_bought, "x", drink_2)
        print (sprite_bought, "x", drink_3)
        print (gatorade_bought, "x", drink_4)
        print (iced_tea_bought, "x", drink_5)
        print (water_bought, "x", drink_6)
        print (doritos_bought, "x", snack_1)
        print (snickers_bought, "x", snack_2)
        print (oreos_bought, "x", snack_3)
        print (lays_bought, "x", snack_4)
        print (bounty_bought, "x", snack_5)
        print (salad_chips_bought, "x", snack_6)
        print ("Change - $", change)
        break
    #When user runs out of money, the items user purchased will be bought and print receipt
    elif change <= 0:
        print ("You have run out of money.")
        print ("\nHere is your transaction details:\n")
        print ("You purchased: ")
        print (coffee_bought, "x", drink_1)
        print (pepsi_bought, "x", drink_2)
        print (sprite_bought, "x", drink_3)
        print (gatorade_bought, "x", drink_4)
        print (iced_tea_bought, "x", drink_5)
        print (water_bought, "x", drink_6)
        print (doritos_bought, "x", snack_1)
        print (snickers_bought, "x", snack_2)
        print (oreos_bought, "x", snack_3)
        print (lays_bought, "x", snack_4)
        print (bounty_bought, "x", snack_5)
        print (salad_chips_bought, "x", snack_6)
        break
    #If user doesn't have enough credit or any error has occured, this message will display
    else:
        print ("There has been an error or you may not have enough credit.")