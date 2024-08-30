import tkinter as tk
root=tk.Tk()
root.geometry("500x200")
root.title("Butoon_state")
root.config(bg="Pink")
tk.Label(root,text="Hello, Welcome to ICCS!").pack(pady=10)
tk.Label(root,text="Indira is one of the Top Computer Science Institute in Pune",bg="red",background="Yellow").pack(pady=10)
text_box=tk.Text(root, selectbackground="yellow",).pack(pady=10)
tk.Label(root,text="HIE").pack(pady=10)
def game1():
    tk.Label(root,text="Anita").pack(pady=10)
def game():
    tk.Button(root,text="Hello, Indira",command=game1).pack(pady=10)

btn=tk.Button(root, text="Start",command=game).pack(pady=10)
root.mainloop()