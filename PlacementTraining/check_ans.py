import tkinter as tk
root=tk.Tk()
root.title("squares and square root game")
def start_game():
    player_name = name_entry.get()
    question_label.config(text=f"Ready,{player_name}? Your question will appear here.")
    answer_entry.config(state=tk.NORMAL)
    submit_button.config(state=tk.NORMAL)
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
