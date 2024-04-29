import random

ran_num = random.randint(1,20)
guess_count = 0
while True:
    user_num = round(float(((input("Guess a number between 1 and 20 (will round to closest int): ")))))
    if user_num < 1 or user_num > 20:
        print("Input wasn't a according to instructions. Try again!")
        guess_count += 1
        continue
    if user_num > ran_num:
        print("Your number is bigger. Try again.")
        guess_count += 1
        continue
    if user_num < ran_num:
        print("Your number is smaller. Try again.")
        guess_count += 1
        continue
    if user_num == ran_num:
        guess_count += 1
        print("Well done! The number is ", ran_num, ". You guessed right! It took you ", guess_count,  " attempts")
        break
