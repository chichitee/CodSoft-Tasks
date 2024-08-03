import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cute Pink Password Generator")
        self.root.geometry("400x300")
        self.root.configure(bg='#FFC0CB')  # Light pink background

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(self.root, text="Password Generator", font=('Arial', 18, 'bold'), bg='#FFC0CB', fg='#000000')
        self.title_label.pack(pady=20)

        # Length Input
        self.length_label = tk.Label(self.root, text="Enter desired length:", font=('Arial', 12), bg='#FFC0CB', fg='#000000')
        self.length_label.pack(pady=5)
        
        self.length_entry = tk.Entry(self.root, font=('Arial', 12), bd=2, relief='solid', width=20, bg='#FFFFFF', fg='#000000')
        self.length_entry.pack(pady=5)

        # Generate Button
        self.generate_button = tk.Button(self.root, text="Generate Password", font=('Arial', 12, 'bold'), bg='#FF69B4', fg='#000000', bd=1, relief='raised', command=self.generate_password)
        self.generate_button.pack(pady=20)

        # Result Label
        self.result_label = tk.Label(self.root, text="", font=('Arial', 14), bg='#FFC0CB', fg='#000000', wraplength=350)
        self.result_label.pack(pady=20)

    def generate_password(self):
        # Get the length from user input
        try:
            length = int(self.length_entry.get())
            if length < 1:
                raise ValueError("Password length must be at least 1.")
        except ValueError as e:
            messagebox.showerror("Input Error", f"Invalid input: {e}")
            return
        
        # Generate the password
        try:
            password = self._generate_password(length)
            self.result_label.config(text=f"Generated Password: {password}")
        except ValueError as e:
            messagebox.showerror("Generation Error", f"Error: {e}")

    def _generate_password(self, length):
        # Define character sets
        letters = string.ascii_letters
        digits = string.digits
        symbols = string.punctuation

        # Combine all characters
        all_characters = letters + digits + symbols

        # Ensure the password includes at least one character from each set if length allows
        if length < 4:
            raise ValueError("Password length should be at least 4 to include all character types.")
        
        password = [
            random.choice(letters),
            random.choice(digits),
            random.choice(symbols),
        ]
        
        # Add random characters to fill up the desired length
        password += random.choices(all_characters, k=length - 3)
        
        # Shuffle the password list to ensure randomness
        random.shuffle(password)
        
        return ''.join(password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
