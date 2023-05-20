
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
from menu import Menu, MenuItems

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

money_machine.report()
coffee_maker.report()

while is_on:
    options = menu.get_items()
    choice = input(f'What would you like to purchase? {options}:')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        print('drink')
        if coffee_maker.is_resource_sufficient(drink):
            coffee_maker.make_coffee(drink)
