import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        
        # Initialize scores
        self.user_score = 0
        self.computer_score = 0
        
        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Frame for buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=20)

        # Rock, Paper, Scissors buttons
        tk.Button(self.button_frame, text="Rock", command=lambda: self.play("rock")).pack(side=tk.LEFT, padx=10)
        tk.Button(self.button_frame, text="Paper", command=lambda: self.play("paper")).pack(side=tk.LEFT, padx=10)
        tk.Button(self.button_frame, text="Scissors", command=lambda: self.play("scissors")).pack(side=tk.LEFT, padx=10)
        
        # Result display
        self.result_label = tk.Label(self.root, text="Make your move!", font=("Helvetica", 16))
        self.result_label.pack(pady=10)

        # Score display
        self.score_label = tk.Label(self.root, text=f"User: {self.user_score} | Computer: {self.computer_score}", font=("Helvetica", 12))
        self.score_label.pack(pady=10)

    def play(self, user_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        
        result = self.determine_winner(user_choice, computer_choice)
        
        # Update scores
        if result == "win":
            self.user_score += 1
            message = f"You win! Computer chose {computer_choice}."
        elif result == "lose":
            self.computer_score += 1
            message = f"You lose! Computer chose {computer_choice}."
        else:
            message = f"It's a draw! Both chose {computer_choice}."
        
        self.result_label.config(text=message)
        self.score_label.config(text=f"User: {self.user_score} | Computer: {self.computer_score}")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "draw"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            return "win"
        else:
            return "lose"

# Create the main application window and run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()
