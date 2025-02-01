# How to Create A Store Calculator & Receipt Generator In Basic Python?

sum = 0
while(True):
    print("Welcome to Store")
    number = input("Enter price:\n")
    if(number !='s'):
        sum = sum + int(number)
        print(f"Total bill so far: {sum}\n")

    else:
        print(f"Your total bill {sum}. Thanks for shopping.")
        break
