MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def report_status():
  print(f"Water: {resources['water']}")
  print(f"Milk: {resources['milk']}")
  print(f"Coffee: {resources['coffee']}")
  print(f"Money: {resources['money']}")

def run_coffee():
  selection = input('What would you like? [espresso, latte, cappucino')
  if selection == 'espresso':
    resources['water'] -= MENU['espresso']['ingredients']['water']
    resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
    quarters = int(input(f"That will cost ${MENU[selection]['cost']}. How many quarters are you using?"))
    dimes = int(input("How many dimes are you using?"))
    nickels = int(input("How many nickels are you using?"))
    quarter = 0.25
    dime = 0.1
    nickel = 0.05
    payment = float((quarters * quarter) + (nickels * nickel) + (dimes * dime))
    if payment >= float(MENU[selection]['cost']):
      change = float(((MENU[selection]['cost']) - payment) * -1)
      print(f'Payment successful. Your change is ${change}')
      resources['money'] += (payment - change)
      run_coffee()
    else:
      print('Not enough money, choose again:')
      run_coffee()
    

  elif selection == 'latte':
    resources['water'] -= MENU['latte']['ingredients']['water']
    resources['milk'] -= MENU['latte']['ingredients']['milk']
    resources['coffee'] -= MENU['latte']['ingredients']['coffee']
    quarters = int(input(f"That will cost ${MENU[selection]['cost']}. How many quarters are you using?"))
    dimes = int(input("How many dimes are you using?"))
    nickels = int(input("How many nickels are you using?"))
    quarter = 0.25
    dime = 0.1
    nickel = 0.05
    payment = float((quarters * quarter) + (nickels * nickel) + (dimes * dime))
    if payment >= float(MENU[selection]['cost']):
      change = float(((MENU[selection]['cost']) - payment) * -1)
      print(f'Payment successful. Your change is ${change}')
      resources['money'] += (payment - change)
      run_coffee()
    else:
      print('Not enough money, choose again:')
      run_coffee()
    
  elif selection == 'cappucino':
    resources['water'] -= MENU['latte']['ingredients']['water']
    resources['milk'] -= MENU['latte']['ingredients']['milk']
    resources['coffee'] -= MENU['latte']['ingredients']['coffee']
    quarters = int(input(f"That will cost ${MENU[selection]['cost']}. How many quarters are you using?"))
    dimes = int(input("How many dimes are you using?"))
    nickels = int(input("How many nickels are you using?"))
    quarter = 0.25
    dime = 0.1
    nickel = 0.05
    payment = float((quarters * quarter) + (nickels * nickel) + (dimes * dime))
    if payment >= float(MENU[selection]['cost']):
      change = float(((MENU[selection]['cost']) - payment) * -1)
      print(f'Payment successful. Your change is ${change}')
      resources['money'] += (payment - change)
      run_coffee
    else:
      print('Not enough money, choose again:')
      run_coffee()
    
  elif selection == 'report':
    report_status()
    run_coffee()
  else:
    print('Invalid Entry.')
    run_coffee()

while resources['milk'] or resources['coffee'] or resources['water'] >= 0:
  run_coffee()
else:
  print('out of service')