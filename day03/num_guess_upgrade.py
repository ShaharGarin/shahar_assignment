import random

MIN = 1
MAX = 20
CHEATER = "cheater, Mccheatinson. tsk tsk."
YES = "Y"
NO = "N"
GOODBYE = "Thanks for playing! See you around, buddy."
EXIT = "x"
NEW_GAME = "n"
NEW_GAME_MSG = "Let's restart!"


def main():
    """
    Main number guessing game loop.
    """
    guess_count = 0
    game_on = True
    cheat_mark =" :)"
    while True:
        if game_on:
            game_num = ran_num(MIN, MAX)
            game_on = False
            guess_count = 0
            cheat_mark = " :)"
        user_guess = get_num()
        guess_count += 1
        if user_guess == CHEATER:
            print(f"Hey. Don't tell anyone, but the number is {game_num}.")
            cheat_mark = " :|"
            guess_count -= 1
            continue
        if user_guess == EXIT:
            print(GOODBYE)
            break
        if user_guess == NEW_GAME:
            another = play_again()
            if another:
                game_on = True
                print(NEW_GAME_MSG)
                continue
            if not another:
                print(GOODBYE)
                break
        if not_num(user_guess):
            continue
        user_num = int(float(user_guess))
        if bad_input(user_num):
            continue
        check = check_num(user_num, game_num)
        if bool(check):
            print(f"Your number is {check}. Try again.")
            continue
        if not bool(check):
            print(f"Well done! The number is {game_num}. You guessed right! It took you {guess_count} attempts{cheat_mark}")
            another = play_again()
            if another:
                game_on = True
                print(NEW_GAME_MSG)
                continue
            if not another:
                print(GOODBYE)
                break

def ran_num(min, max):
    """
    Function that creates a rundom number.
    """
    ran_num = random.randint(min,max)
    return ran_num

def get_num():
    """
    Function that gets an input from the user. Checks for user commands and returns the command. If the input wasn't a command, it returns the original input.
    """
    user_num = input(f"Guess a number between {MIN} and {MAX} (will round to closest int). Input 'x' to exit, 'n' to start a new game. ")
    if user_num == "x":
        return EXIT
    if user_num == "n":
        return NEW_GAME
    if user_num == "s":
        user_num = CHEATER
    return user_num

def not_num(input):
    """
    Makes sure that the input is a number.
    """
    if not input.isnumeric() and EXIT and NEW_GAME and CHEATER:
        print("Only numbers are applicable. Try again.")
        return True
    return False

def bad_input(input):
    """
    Checks the inputed number is in range.
    """
    if input < MIN or input > MAX:
        print("Input wasn't in range. Try again!")
        return True
    return False

def check_num(input, target):
    """
    Compares unputed number to target number.
    """
    if input > target:
        return "bigger"
    if input < target:
        return "smaller"
    if input == target:
        return 0

def play_again():
    """
    Asks the user if they want to play again.
    """
    while True:
        more = input("Would you like to go another round (Y/N)?")
        if more == YES:
            return True
        if more == NO:
            return False
        else:
            print("Pick 'Y' or 'N' only: ")
            continue

main()
