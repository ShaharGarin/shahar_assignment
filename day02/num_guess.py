import random
min = 1
max = 20

ran_num = random.randint(min,max)
guess_count = 0

while True:
    user_num = input("Guess a number between 1 and 20 (will round to closest int): ")
    guess_count += 1
    if not user_num.isnumeric():
        print("Only numbers are applicable. Try again.")
        continue
    user_num = int(float(user_num))
    if user_num < min or user_num > max:
        print("Input wasn't in range. Try again!")
        continue
    if user_num > ran_num:
        print("Your number is bigger. Try again.")
        continue
    if user_num < ran_num:
        print("Your number is smaller. Try again.")
        continue
    if user_num == ran_num:
        print(f"Well done! The number is {ran_num}. You guessed right! It took you {guess_count} attempts")
        break
