import tkinter as tk
import math
import random
import time
root=tk.Tk()
root.title("squares and square root game")
'''def is_perfect_square(n):
    return math.isqrt(n)**2==n

def display_processing_bar():
    for _ in range(10):

        time.sleep(0.2)
        progress_label=tk.Label(root,text="Processing")'''

def ask_square_question():
    num=random.randint(1,100)
    correct_answer=num**2
    question_label.config(text=f"What is square of{num}?")
    return correct_answer

def ask_square_root_question():
    num=random.randint(1,1000)
    while not is_perfect_square(num):
        num=random.randint(1,1000)
    correct_answer=int(math.sqrt(num))
    question_label.config(text=f"What is the square root of {num}?")
    return correct_answer

def start_game():
    player_name = name_entry.get()
    question_label.config(text=f"Ready,{player_name}? Your question will appear here.")
    answer_entry.config(state=tk.NORMAL)
    submit_button.config(state=tk.NORMAL)
    continue_game()


def continue_game():
    global correct_answer
    answer_entry.delete(0,tk.END)
    question_type=random.choice(["square","squareroot"])
    if question_type=="square":
        correct_answer=ask_square_question()
    else:
        correct_answer=ask_square_root_question()
def check_answer():
    print(f"Checking answer:{answer_entry.get()}")
    result_label.config(text=f"Your answer")
    progress_label.config(text=f"Progress")
def quit():
    root.quit()

tk.Label(root,text="Welcome to the Squares and Square roots Game!").pack(pady=10)
tk.Label(root,text="plz enter your name:").pack(pady=5)
name_entry=tk.Entry(root)
name_entry.pack(pady=5)


start_button=tk.Button(root,text="start game",command=start_game)
start_button.pack(pady=10)

submit_button=tk.Button(root,text="Submit Answer",state=tk.DISABLED,command=check_answer)
submit_button.pack(pady=10)

result_label=tk.Label(root,text="",font=("PUBG",14))
result_label.pack(pady=10)

progress_label=tk.Label(root,text="",font=("PUBG",14))
progress_label.pack(pady=10)

quit_button=tk.Button(root,text="Submit Answer",state=tk.DISABLED,command=quit)
quit_button.pack(pady=10)

question_label=tk.Label(root,text="",font=("PUBG",14))
question_label.pack(pady=10)

answer_entry = tk.Label(root,text="",font=("PUBG",14))
answer_entry.pack(pady=10)

root.mainloop()
