import tkinter as tk
root=tk.Tk()
root.config(bg="pink")


def start_game():
    player_name=name_entry.get()
    question_label.config(text=f"Ready,{player_name}? Your question will appear here.")
    answer_entry.config(state=tk.NORMAL)

tk.Label(root,text="Welcome to the Squares and Square root Game!").pack(pady=10)
tk.Label(root,text="Please enter your name:").pack(pady=5)
name_entry=tk.Entry(root)
name_entry.pack(pady=5)


start_button=tk.Button(root,text="Start Game",bg="Yellow",command=start_game)
start_button.pack(pady=10)

question_label=tk.Label(root,text="",font=("Pubg",14))
question_label.pack(pady=10)

tk.Label(root,text="Your answer:").pack(pady=5)
answer_entry=tk.Entry(root,state=tk.DISABLED)
answer_entry.pack(pady=10)

root.mainloop()

