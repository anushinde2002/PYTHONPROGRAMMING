import tkinter as tk
from tkinter import messagebox


class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Form")
        self.root.geometry("300x200")

        # Username Label and Text Entry Box
        tk.Label(root, text="Username").pack(pady=10)
        self.username = tk.Entry(root)
        self.username.pack(pady=5)

        # Password Label and Password Entry Box
        tk.Label(root, text="Password").pack(pady=10)
        self.password = tk.Entry(root, show='*')
        self.password.pack(pady=5)

        # Login Button
        tk.Button(root, text="Login", command=self.login).pack(pady=20)

        # Message Label
        self.message = tk.Label(root, text="", fg="red")
        self.message.pack(pady=5)

    def login(self):
        username = self.username.get()
        password = self.password.get()

        # Simple hardcoded check for demonstration purposes
        if username == "admin" and password == "password":
            self.message.config(text="Login successful!", fg="green")
        else:
            self.message.config(text="Invalid credentials", fg="red")


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
