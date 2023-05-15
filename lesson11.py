import random
import os

play = input('Welcome to blackjack, do you want to play? [y/n]')


def clear_terminal():
    # Clear terminal command for Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # Clear terminal command for macOS and Linux
    else:
        _ = os.system('clear')


user_cards = []
computer_cards = []

def calculate_score(user_cards, computer_cards):
  global user_score
  global computer_score
  user_score = 0
  computer_score = 0
  for cards in user_cards:
    user_score += int(cards)
  for cards in computer_cards:
    computer_score += int(cards)
  print(f"Your score: {user_score} Computer's score: XX")

def blackjack_checker(user_cards, computer_cards):
  if user_cards == [11, 10] or user_cards == [10,11]:
    print('Blackjack! You won!')
    if computer_cards == [11, 10] or computer_cards == [10,11]:
      print('Blackjack! The computer won!')
  

def deal_card():
  user_cards = []
  computer_cards = []
  hit = 'y'
  
  while hit == 'y':
    clear_terminal()
    for _ in range(1):
      user_cards.append(random.choice(cards))
      computer_cards.append(random.choice(cards))
      print(f'users {user_cards} computer = XX')
      blackjack_checker(user_cards, computer_cards)
      calculate_score(user_cards, computer_cards)
      hit = input('Do you want to hit another card? [y/n]')
  else:
    if user_score > computer_score and user_score < 22:
      print('user wins')
      status = input('Play again [y/n]')
      if status == 'y':
        deal_card()
      else:
        print('game over')
    elif computer_score > user_score and computer_score < 22:
      print('computer wins')
      status = input('Play again [y/n]')
      if status == 'y':
        deal_card()
      else:
        print('game over')
    else:
      print('tie')
      status = input('Play again [y/n]')
      if status == 'y':
        deal_card()
      else:
        print('game over')
    


          
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

if play == 'y':
  deal_card()
else:
  print('Okay, bye!')

