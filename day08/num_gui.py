import random
import tkinter as tk


min = 1
max = 20
ran_num = random.randint(min,max)
smiley = ":)"

#Create gui window
gui = tk.Tk()
gui.title("The Number Guessing Game!")
gui.geometry('640x480')
lbl = tk.Label(gui, text = "Can you guess a nubmer between 1 and 20?")
lbl.grid()
warning = tk.Label(gui, text = "")
warning.grid(row = 1, column = 0)
#Create user entry
user_guess = tk.Entry(gui, width = 2)
user_guess.grid(row = 0, column = 1, padx = 3)
guess_var = 0
guess_count = tk.Label(gui, text = f"Number of guesses: {guess_var}")
guess_count.grid(row = 2, column = 0)
cheat_lbl = tk.Label(gui, text = "")
cheat_lbl.grid(row = 4, column = 0, sticky = 's')

def start_game():
    global guess_var, ran_num, smiley
    guess_var = 0
    smiley = ":)"
    guess_count.config(text = f"Number of guesses: {guess_var}")
    ran_num = random.randint(min,max)
    warning.config(text = "")

def main_game():
    global guess_var, warning
    cur_guess = user_guess.get()
    guess_var += 1
    guess_count.config(text = f"Number of guesses: {guess_var}")
    if not cur_guess.isnumeric():
       warning.config(text = "Not an integer. Try again.")
    if int(cur_guess) < min or int(cur_guess) > max:
        warning.config(text = "Number out of range. Tray again.")
    elif int(cur_guess) < ran_num:
        warning.config(text = "Try a larger number.")
    elif int(cur_guess) > ran_num:
        warning.config(text = "Try a smaller number.")
    else:
        warning.config(text = f"YOU DID IT! WELL DONE {smiley}")
        
def cheater():
    global smiley, cheat_lbl
    smiley = ":/"
    cheat_lbl.config(text = f"You naughty cheater, you. The number is {ran_num}")


#Create buttons
start_butt = tk.Button(text = "Restart Game", command = start_game)
start_butt.grid(row = 3, column = 0)
guess_butt = tk.Button(text = "Guess!", command = main_game)
guess_butt.grid(row = 0, column = 2)
exit_butt = tk.Button(text = "Exit", command = exit)
exit_butt.grid(row = 3, column = 1)
cheat_butt = tk.Button(text = "I'm a cheater",bd = 0, fg = 'grey', command = cheater)
cheat_butt.grid(row = 4, column = 3, sticky = 'se')
gui.grid_rowconfigure(4, weight = 2)

gui.mainloop()
