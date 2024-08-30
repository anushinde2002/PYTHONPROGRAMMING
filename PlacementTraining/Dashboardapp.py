import tkinter as tk
from tkinter import ttk

class DashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard")
        self.root.geometry("800x600")

        # Create a menu bar
        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)

        # Add file menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=root.quit)

        # Add help menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About")

        # Create a frame for the left menu
        left_menu_frame = tk.Frame(root, bg="lightgrey", width=200)
        left_menu_frame.pack(side="left", fill="y")

        # Add buttons to the left menu
        tk.Button(left_menu_frame, text="Home", width=20, command=self.show_home).pack(pady=10)
        tk.Button(left_menu_frame, text="Profile", width=20, command=self.show_profile).pack(pady=10)
        tk.Button(left_menu_frame, text="Settings", width=20, command=self.show_settings).pack(pady=10)

        # Create a main content frame
        self.main_content_frame = tk.Frame(root, bg="white")
        self.main_content_frame.pack(side="right", expand=True, fill="both")

        # Show home screen by default
        self.show_home()

    def clear_main_content(self):
        for widget in self.main_content_frame.winfo_children():
            widget.destroy()

    def show_home(self):
        self.clear_main_content()
        tk.Label(self.main_content_frame, text="Welcome to the Home Page", font=("Arial", 24)).pack(pady=20)

    def show_profile(self):
        self.clear_main_content()
        tk.Label(self.main_content_frame, text="User Profile", font=("Arial", 24)).pack(pady=20)
        tk.Label(self.main_content_frame, text="Name: Anu Shinde", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.main_content_frame, text="Email: anushinde2502@gmail.com ", font=("Arial", 14)).pack(pady=10)

    def show_settings(self):
        self.clear_main_content()
        tk.Label(self.main_content_frame, text="Settings", font=("Arial", 24)).pack(pady=20)
        tk.Label(self.main_content_frame, text="Settings option 1", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.main_content_frame, text="Settings option 2", font=("Arial", 14)).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = DashboardApp(root)
    root.mainloop()
