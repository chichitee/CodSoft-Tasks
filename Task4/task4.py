import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")
        self.root.geometry("400x400")
        self.root.configure(bg='#FFC0CB')  # Light pink background

        self.user_score = 0
        self.computer_score = 0

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(self.root, text="Rock, Paper, Scissors", font=('Arial', 18, 'bold'), bg='#FFC0CB', fg='#000000')
        self.title_label.pack(pady=20)

        # Instructions Label
        self.instructions_label = tk.Label(self.root, text="Choose Rock, Paper, or Scissors:", font=('Arial', 12), bg='#FFC0CB', fg='#000000')
        self.instructions_label.pack(pady=10)

        # Buttons for choices
        self.button_frame = tk.Frame(self.root, bg='#FFC0CB')
        self.button_frame.pack(pady=10)

        self.rock_button = tk.Button(self.button_frame, text="Rock", font=('Arial', 12), bg='#FF69B4', fg='#000000', command=lambda: self.play('rock'))
        self.rock_button.grid(row=0, column=0, padx=10, pady=10)

        self.paper_button = tk.Button(self.button_frame, text="Paper", font=('Arial', 12), bg='#FF69B4', fg='#000000', command=lambda: self.play('paper'))
        self.paper_button.grid(row=0, column=1, padx=10, pady=10)

        self.scissors_button = tk.Button(self.button_frame, text="Scissors", font=('Arial', 12), bg='#FF69B4', fg='#000000', command=lambda: self.play('scissors'))
        self.scissors_button.grid(row=0, column=2, padx=10, pady=10)

        # Result and Score Labels
        self.result_label = tk.Label(self.root, text="", font=('Arial', 14), bg='#FFC0CB', fg='#000000', wraplength=350)
        self.result_label.pack(pady=20)

        self.score_label = tk.Label(self.root, text=f"Score - You: {self.user_score} | Computer: {self.computer_score}", font=('Arial', 12), bg='#FFC0CB', fg='#000000')
        self.score_label.pack(pady=10)

        # Play Again Button
        self.play_again_button = tk.Button(self.root, text="Play Again", font=('Arial', 12, 'bold'), bg='#FF69B4', fg='#000000', command=self.play_again, state=tk.DISABLED)
        self.play_again_button.pack(pady=20)

    def play(self, user_choice):
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)
        
        # Determine winner
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            result = "You win!"
            self.user_score += 1
        else:
            result = "You lose!"
            self.computer_score += 1
        
        # Update result and score
        self.result_label.config(text=f"You chose {user_choice}. Computer chose {computer_choice}. {result}")
        self.score_label.config(text=f"Score - You: {self.user_score} | Computer: {self.computer_score}")
        
        # Enable Play Again button
        self.play_again_button.config(state=tk.NORMAL)

    def play_again(self):
        # Clear result label and disable Play Again button
        self.result_label.config(text="")
        self.play_again_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()
