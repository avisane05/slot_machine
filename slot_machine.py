MAX_LINE = 3
MIN_BET = 1
MAX_BET = 100

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
    bet = get_bet()
    print(balance, lines, bet)

main()
