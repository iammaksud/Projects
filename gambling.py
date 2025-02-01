import random

MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "c": 6,
    "D": 8
}

def get_slot_machine_spin(rows,cols,symbols):
    

def deposit():
    while True:
        amount = input("Your deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Enter a valid number!")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines on (1-" + str(MAX_LINE) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINE:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Enter a valid number!")

    return lines


def get_bet():
    while True:
        amount = input("Your bet per line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number!")

    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet

        if total_bet > balance:
            print(f"you do not have enough money, your current balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines.")
    print(f"Total bet is equal to ${total_bet}")

main()