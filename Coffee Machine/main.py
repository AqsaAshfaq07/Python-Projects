# from replit import clear
from menu import menu, resources


def manage_resources(coins):
    resources['water'] -= menu[choice]['ingredients']['water']
    resources['milk'] -= menu[choice]['ingredients']['milk']
    resources['coffee'] -= menu[choice]['ingredients']['coffee']
    resources['money'] += coins


def main(choice):
    # Check resources
    if resources['water'] >= menu[choice]['ingredients']['water']:
        if resources['milk'] >= menu[choice]['ingredients']['milk']:
            if resources['coffee'] >= menu[choice]['ingredients']['coffee']:
                # Process Coins

                pennies = int(input("Insert Coins: \nHow many pennies: "))
                nickles = int(input("How many nickles: "))
                dimes = int(input("How many dimes: "))
                quarters = int(input("How many quarters: "))

                coins = round((pennies * 0.01 + nickles * 0.05 + dimes * 0.10 + quarters * 0.25), 2)

                # Check Transaction is Successful or Not!

                if coins == menu[choice]['cost']:
                    print(f"Here is your {choice}. Enjoy ☕")
                    manage_resources(coins)

                elif coins > menu[choice]['cost']:
                    manage_resources(coins)
                    change = round((coins - menu[choice]['cost']), 2)
                    print(
                        f"Here is your ${change} in change.  \nHere is your {choice}. Enjoy ☕"
                    )

                else:
                    print("Sorry that's not enough Money.\nMoney Refunded!")
                    # clear()

            else:
                print("Sorry there is not enough Coffee.")
        else:
            print("Sorry there is not enough Milk.")
    else:
        print("Sorry there is not enough Water.")




should_continue = True
while should_continue:
    choice = input(
        "What would you like? (espresso / latte / cappuccino): ").lower()
    if choice == 'latte' or choice == 'cappuccino' or choice == 'espresso':
        main(choice)
        continue

    elif choice == 'off':
        should_continue = False

    elif choice == 'report':
        # give_report(choice)
        print(f"water: {resources['water']}ml    \nmilk: {resources['milk']}ml   \ncoffee: {resources['coffee']}g    \nmoney: ${round((resources['money']), 2)}")

    else:
        print("Please enter a valid input!")
        continue
