#lab4

#task1
checking = "yes"

while checking == "yes":
    print("what is your age")
    user_input = input()

    if int(user_input) >= 18:
        print("yes you can vote")
    else:
       print("you cant vote")
       print ("would you like to check another age?")
       user_input2 = input()
       checking = user_input2

#task2
numbers = (15, -7, 0, 23, -42, 8)
for number in numbers:
    if number > 0:
        print(  f"{number} is positive")
    elif number < 0:
        print (  f"{number} is negative")
    else:
        print( f"{number} is zero")

#task3
inventory="iron", "redstone", "watermelone", "woodb", "nertherite","totome of on dying"
for block in inventory:
    print(f"{block} is in the inventory")
    if block== "totome of on dying":
        print("jackpot! you found an totome of on dying!")

