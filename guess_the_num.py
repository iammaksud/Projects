import random 


comcho = random.randint(1,100)
while True:
    try:
        user = int(input("Enter the number: "))
        print(f'You choose: {user}')

        if comcho == user:
            print('You win buddy!')
            break
        elif comcho > user:
            print('Too Low!')
        else:
            print('Too High!')
            
    except ValueError:
        print('Enter a valid number')