# Rock Paper Scissors

import random

emojis = { 'r': '🪨', 'p': '📃', 's': '✂️'}
choices = ('r', 'p', 's')

while True:
    userCho= input('Rock, paper, or scissors?: ').lower()
    if userCho not in choices:
      print('Invalid choice!')
      continue

    comCho = random.choice(choices)
      
    print(f'YOU CHOICE {emojis[userCho]}')
    print(f'COMPUTER CHOICE {emojis[comCho]}')

    if userCho == comCho:
        print('Tie!')
    elif (
        (userCho == 'r' and comCho == 's') or 
        (userCho == 's' and comCho == 'p') or 
        (userCho == 'p' and comCho == 'r')):
        print('You win')
    else:
        print('You lose')  


    again = input('Wanna play again? (y/n): ').lower()
    if again== 'n':
        print('Thanks for palying!')
        break

