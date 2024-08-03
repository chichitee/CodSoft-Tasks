import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cute Pink Calculator")
        self.root.geometry("300x400")
        self.root.configure(bg='#FFC0CB')  # Light pink background

        self.create_widgets()

    def create_widgets(self):
        # Entry widget to display numbers and results
        self.result_var = tk.StringVar()
        self.result_entry = tk.Entry(self.root, textvariable=self.result_var, font=('Arial', 18), bd=2, relief='solid', justify='right', bg='#FFFFFF', fg='#000000')
        self.result_entry.pack(pady=20, padx=10, fill=tk.X)

        # Button frame
        self.button_frame = tk.Frame(self.root, bg='#FFC0CB')
        self.button_frame.pack()

        # Button configurations
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0)  # Clear button
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.button_frame, text=text, font=('Arial', 14), bg='#FF69B4', fg='#000000', bd=1, relief='raised', width=5, height=2,
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, char):
        current_text = self.result_var.get()

        if char in '0123456789.':
            self.result_var.set(current_text + char)
        elif char in '+-*/':
            self.result_var.set(current_text + ' ' + char + ' ')
        elif char == '=':
            try:
                result = eval(current_text)
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid input or calculation error.")
                self.result_var.set('')
        elif char == 'C':
            self.result_var.set('')  # Clear the entry field
        else:
            self.result_var.set('')

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
