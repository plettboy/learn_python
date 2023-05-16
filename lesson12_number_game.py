#SCOPE AND GLOBAL SCOPE
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
answer = random.randint(1,101)


rabbit_art = '''
                              __
                     /\    .-" /
                    /  ; .'  .' 
                   :   :/  .'   
                    \  ;-.'     
       .--""""--..__/     `.    
     .'           .'    `o  \   
    /                    `   ;  
   :                  \      :  
 .-;        -.         `.__.-'  
:  ;          \     ,   ;       
'._:           ;   :   (        
    \/  .__    ;    \   `-.     
     ;     "-,/_..--"`-..__)    
     '""--.._:
'''

print(rabbit_art)


print("Welcome to the guessing game. \nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
global attempts
attempts = 0
if difficulty == 'easy':
  attempts += 10
else: attempts += 5
print(f'You have {attempts} attempts to guess the number.')

def game_over():
    print('Game over. You lost')
    print(f'The answer was {answer}.')
    

def guess_func():
  global attempts
  guess = int(input('Make a guess:'))
  if guess > answer:
    print('Too high')
    attempts -= 1
    print(f'You have {attempts} attempts left. ')
    if attempts == 0:
      game_over()
    else:
      guess_func()
  elif guess < answer:
    print('Too low')
    attempts -= 1
    print(f'You have {attempts} attempts left. ')
    if attempts == 0:
      game_over()
    else:
      guess_func()
  elif guess == answer:
    print('You got it!')
    print(f'You Win!!')
    

guess_func()
  