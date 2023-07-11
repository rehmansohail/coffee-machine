import menu

def check_ingredients(order):
    if water<menu.MENU[order]["ingredients"]["water"]:
        return "Sorry, there isn't enough water."
    if milk < menu.MENU[order]["ingredients"]["milk"]:
        return "Sorry, there isn't enough milk."
    if coffee < menu.MENU[order]["ingredients"]["coffee"]:
        return "Sorry, there isn't enough coffee."
    return "ok"


water = 300
milk = 200
coffee = 100
money = 0

flag = input("What do you need? 'espresso', 'latte' or 'cappuccino'\n").lower()
while 1:
    if flag == "off":
        break
    elif flag == "report":
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}gm")
        print(f"Money: ${money}")
    elif flag == "espresso" or flag == "latte" or flag == "cappuccino":
        temp = 0
        n = int(input("How many quarters you have?\n"))
        temp += n*0.25
        n = int(input("How many dimes you have?\n"))
        temp += n*0.10
        n = int(input("How many nickles you have?\n"))
        temp += n*0.05
        n = int(input("How many pennies you have?\n"))
        n += n*0.01
        if flag == "espresso":
            st = check_ingredients(flag)
            if st == "ok":
                if temp >= menu.MENU[flag]["cost"]:
                    change = round(temp - menu.MENU[flag]["cost"],2)
                    water -= menu.MENU[flag]["ingredients"]["water"]
                    milk -= menu.MENU[flag]["ingredients"]["milk"]
                    coffee -= menu.MENU[flag]["ingredients"]["coffee"]
                    money += menu.MENU[flag]["cost"]
                    print(f"Enjoy your espresso, here is your change ${change}")
                else:
                    print("You have insufficient money")
            else:
                print(st)
                print("Here is your money back")
        elif flag == "latte":
            st = check_ingredients(flag)
            if st == "ok":
                if temp >= menu.MENU[flag]["cost"]:
                    change = temp - menu.MENU[flag]["cost"]
                    water -= menu.MENU[flag]["ingredients"]["water"]
                    milk -= menu.MENU[flag]["ingredients"]["milk"]
                    coffee -= menu.MENU[flag]["ingredients"]["coffee"]
                    money += menu.MENU[flag]["cost"]
                    print(f"Enjoy your latte, here is your change ${change}")
                else:
                    print("You have insufficient money")
            else:
                print(st)
                print("Here is your money back")
        else:
            st = check_ingredients(flag)
            if st == "ok":
                if temp >= menu.MENU[flag]["cost"]:
                    change = temp - menu.MENU[flag]["cost"]
                    water -= menu.MENU[flag]["ingredients"]["water"]
                    milk -= menu.MENU[flag]["ingredients"]["milk"]
                    coffee -= menu.MENU[flag]["ingredients"]["coffee"]
                    money += menu.MENU[flag]["cost"]
                    print(f"Enjoy your cappuccino, here is your change ${change}")
                else:
                    print("You have insufficient money")
            else:
                print(st)
                print("Here is your money back")


    else:
        print("Invalid input")

    flag = input("What do you need? 'espresso', 'latte' or 'cappuccino'\n").lower()
