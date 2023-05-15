#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = []

rand_letters = letters[random.randint(0,27)]
rand_numbers = numbers[random.randint(1,10)]
rand_symbols = symbols[random.randint(1,9)]

for pass_letters in range(0,nr_letters):
  password.append(rand_letters)

for pass_numbers in range(0,nr_numbers):
  password.append(rand_numbers)

for pass_symbols in range(0,nr_symbols):
  password.append(rand_symbols)

random.shuffle(password)
password = ''.join(password)
print(password)