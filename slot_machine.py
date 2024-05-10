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

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    # transposing matrix
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])
    

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


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your currunt balance is: Rs.{balance}")
        else:
            break

    print(f"You are betting Rs.{bet} on {lines}. Total bet is equal to: RS.{total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winning, winning_lines = check_winnings(slots, lines, bet, symbol_values)

    print(f"You win Rs.{winning}")
    print(f"You win on line:", *winning_lines)

    return winning - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is Rs.:{balance}")
        answer = input("Press enter to Play (Press q to quit) ").lower()

        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with Rs.{balance}")

main()
