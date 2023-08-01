from menu import Menu, MenuItem
from coffee_makear import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

should_continue = True

while should_continue:
  options = menu.get_items()
  choice = (input(f"What would you like? ({options}): ")).lower()
  if choice == "off":
    print("Good luck! See you next time:)")
    should_continue = False
  elif choice == "report":
    coffee_maker.report()
    money_machine.report()
  elif choice not in options:
    print("Sorry that item isn't avaiable")
    continue
  else:
    drink = menu.find_drink(choice)

    if coffee_maker.is_resource_sufficient(
        drink) and money_machine.make_payment(drink.cost):
      coffee_maker.make_coffee(drink)
