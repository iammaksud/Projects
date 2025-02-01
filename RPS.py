# Rock Paper Scissors

import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
emojis = { ROCK: '🪨', PAPER: '📃', SCISSORS: '✂️'}
choices = tuple(emojis.keys())

def get_userCho():
  while True:
    userCho= input('Rock, paper, or scissors?: ').lower()
    if userCho in choices:
      return userCho
    else:
       print('Invalid choice!')
def displayCho(userCho,comCho):
   print(f'YOU CHOICE {emojis[userCho]}')
   print(f'COMPUTER CHOICE {emojis[comCho]}')

def winner(userCho,comCho):
    if userCho == comCho:
        print('Tie!')
    elif (
        (userCho == ROCK and comCho == SCISSORS) or 
        (userCho == SCISSORS and comCho == PAPER) or 
        (userCho == PAPER and comCho == ROCK)):
        print('You win')
    else:
        print('You lose')     
def palyGame():
    while True:
        userCho = get_userCho()

        comCho = random.choice(choices)

        displayCho(userCho,comCho) 
        
        winner(userCho,comCho)    

        again = input('Wanna play again? (y/n): ').lower()
        if again == 'n':
            print('Thanks for palying!')
            break

palyGame()