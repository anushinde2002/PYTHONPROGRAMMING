import tkinter as tk
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.expression = ""

        self.input_text = tk.StringVar()

        input_frame = tk.Frame(self.root)
        input_frame.pack()

        input_field = tk.Entry(input_frame, textvariable=self.input_text, font=('arial', 18, 'bold'), bd=10,
                               insertwidth=4, width=14, justify='right')
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        button_frame = tk.Frame(self.root)
        button_frame.pack()

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0)
        ]

        for (text, row, col) in buttons:
            if text == '=':
                button = tk.Button(button_frame, text=text, width=32, height=3, bd=0, bg='#eee', cursor='hand2',
                                   command=self.equal)
            elif text == 'C':
                button = tk.Button(button_frame, text=text, width=32, height=3, bd=0, bg='#f00', cursor='hand2',
                                   command=self.clear)
            else:
                button = tk.Button(button_frame, text=text, width=10, height=3, bd=0, bg='#fff', cursor='hand2',
                                   command=lambda txt=text: self.btn_click(txt))

            button.grid(row=row, column=col, padx=1, pady=1)

    def btn_click(self, item):
        self.expression = self.expression + str(item)
        self.input_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_text.set("")

    def equal(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except:
            self.input_text.set("error")
            self.expression = ""


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
