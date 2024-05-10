import random

MAX_LINE = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = [[], [], []]

    for _ in range(cols):
        column = []
        currunt_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(currunt_symbols)
            currunt_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def deposit():
    while True:
        amount = input("What would you link to deposit? Rs.")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater then 0.")
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet on (1-" + str(MAX_LINE)+ ")? ")
        if lines.isdigit():
            lines = int(lines)
            if  1 <= lines <= MAX_LINE:
                break
            else:
                print("Enter valid number.")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    while True:
        deposit = input("What would you like to bet on each line? Rs.")
        if deposit.isdigit():
            deposit = int(deposit)
            if  MIN_BET <= deposit <= MAX_BET:
                break
            else:
                print(f"Amound must be between Rs.{MIN_BET} - Rs.{MAX_BET}.")
        else:
            print("Please enter a number.")

    return deposit


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your currunt balance is: Rs.{balance}")
        else:
            break

    print(f"You are betting Rs.{bet} on {lines}. Total bet is equal to: RS.{total_bet}")

    

main()
