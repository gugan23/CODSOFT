import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.root.geometry('2000x1000')

        self.bg_image = ImageTk.PhotoImage(Image.open(r"C:\Users\gugan\Desktop\CODSOFT PROGRAMS\Rock-Paper-Scissor\Cool-Red-and-Black.png"))
        self.l1 = tk.Label(root, image=self.bg_image)
        self.l1.place(x=0, y=0)

        tk.Label(root, text="Choose Rock, Paper, or Scissors:", bg='red2', fg='black', font=('Helvetica', 16)).place(x=600, y=350)

        self.rock_button = tk.Button(root, text="Rock", bg='red', relief='sunken', bd=8, font=('Helvetica', 14), command=lambda: self.user_choice('Rock'))
        self.rock_button.place(x=600, y=450)

        self.paper_button = tk.Button(root, text="Paper", bg='green', relief='sunken', bd=8, font=('Helvetica', 14), command=lambda: self.user_choice('Paper'))
        self.paper_button.place(x=700, y=450)

        self.scissors_button = tk.Button(root, text="Scissors", relief='sunken', bd=8, bg='orange', font=('Helvetica', 14), command=lambda: self.user_choice('Scissors'))
        self.scissors_button.place(x=800, y=450)

        self.result_label = tk.Label(root, text="", bg='black', fg='white', font=('Helvetica', 16))
        self.result_label.pack(pady=20)

        self.exit_button = tk.Button(root, text="Exit", bg='black',fg='white', relief='sunken', bd=8, font=('Helvetica', 14), command=self.exit_game)
        self.exit_button.place(x=700, y=550)

        self.user_score = 0
        self.comp_score = 0
        self.game_count = 0

    def determine_winner(self, user_choice, comp_choice):
        if user_choice == comp_choice:
            return "It's a tie!"
        elif (user_choice == 'Rock' and comp_choice == 'Scissors') or \
             (user_choice == 'Paper' and comp_choice == 'Rock') or \
             (user_choice == 'Scissors' and comp_choice == 'Paper'):
            self.user_score += 1
            return "You win!"
        else:
            self.comp_score += 1
            return "You lose!"

    def user_choice(self, choice):
        comp_choice = random.choice(['Rock', 'Paper', 'Scissors'])
        result = self.determine_winner(choice, comp_choice)
        self.result_label.config(text=f"Computer chose: {comp_choice}\n{result}")
        self.game_count += 1
        if self.game_count == 10:
            if self.user_score > self.comp_score:
                messagebox.showinfo("Game Over", f"You win with a score of {self.user_score} to {self.comp_score}")
            elif self.user_score < self.comp_score:
                messagebox.showinfo("Game Over", f"Computer wins with a score of {self.comp_score} to {self.user_score}")
            else:
                messagebox.showinfo("Game Over", f"It's a tie with a score of {self.user_score} to {self.comp_score}")

            
            self.user_score = 0
            self.comp_score = 0
            self.game_count = 0
            self.result_label.config(text="")

    def exit_game(self):
        response = messagebox.askyesno("Exit Game", "Do you want to exit the game or play again?")
        if response:
            self.root.destroy()
        else:
            self.user_score = 0
            self.comp_score = 0
            self.game_count = 0
            self.result_label.config(text="")

root = tk.Tk()
game = RockPaperScissors(root)
root.mainloop()
