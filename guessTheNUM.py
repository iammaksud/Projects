import random 


def get_user():
    while True:
        try:
            user = int(input("Enter the number: "))
            print(f'You choose: {user}')
            return user
        except ValueError:
            print('Enter a valid number')    

def guess_that():
    comcho = random.randint(1,100)
    while True:
        user = get_user()
        if comcho == user:
            print('You win buddy!')
            break
        elif comcho > user:
            print('Too Low!')
        else:
            print('Too High!')
            
guess_that()            