#random integers
#import the random integer
import random

rand_int = random.randint(1,5)
print(rand_int)

# randint is a module, module is like a method
# to create modules create a new module in a new python file
import lesson4_module as my_module

print(my_module.pi)

#random_floats

random_float = random.random()
#to make a random to a rang of 5.0
print(random_float + rand_int)
#or!
random_float_five = random.random() * 5
print(random_float_five)

love_score = random.randint(1,100)
print(f'yo love score is {love_score}')

#understanding offset and appending
#WITH PYTHON LISTS
#lists are stored like
#fruits = ['item1', 'item2']

fruit = ['apple', 'orange', 'nana']
print(fruit[2])
#to replace values
fruit[2] = 'banana'
print(fruit[2])

#to append 1 item to the end of the list
fruit.append('grape')
print(fruit)

#to add 1 list to another, or multiple items
fruit.extend(['peach', 'plum'])
print(fruit)
#ROCK PAPER SCISSORS GAME
# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1

import random

game = ['rock', 'paper', 'Scissors']
result = random.randint(0,2)

answer = input('What do you choose, 0 for rock, 1 for paper, 2 for scissors?')
print(game[result])
answer = int(answer)

if answer == 0 and game[result] == 'rock':
    print(f'{game[result]}, you tied')
elif answer == 0 and game[result] == 'paper':
    print(f'{game[result]}, you lose')
elif answer == 0 and game[result] == 'Scissors':
    print(f'{game[result]}, you win')
elif answer == 1 and game[result] == 'rock':
    print(f'{game[result]}, you win')
elif answer == 1 and game[result] == 'paper':
    print(f'{game[result]}, you tied')
elif answer == 1 and game[result] == 'Scissors':
    print(f'{game[result]}, you lose')
elif answer == 2 and game[result] == 'rock':
    print(f'{game[result]}, you lose')
elif answer == 2 and game[result] == 'paper':
    print(f'{game[result]}, you win')
elif answer == 2 and game[result == 'Scissors']:
    print(f'{game[result]}, you tied')
else:
    print('enter a valid number between 0 - 2')
