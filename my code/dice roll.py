import random
import time
import tkinter as tk
from tkinter import messagebox

# 🎯 Create main window 
root = tk.Tk()
root.title("🎲 Dice Rolling Simulator")
root.geometry("400x400")
root.config(bg="#222222")

# 🎲 Dice faces (Unicode characters)
dice_faces = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]

# 🎯 Label to display dice face
dice_label = tk.Label(root, text="", font=("Helvetica", 150), fg="white", bg="#222222")
dice_label.pack(pady=50)

# 🎯 Function to roll dice
def roll_dice():
    dice_label.config(text="🎲")
    root.update()
    time.sleep(0.5)  # short delay for animation

    # generate random face
    value = random.choice(dice_faces)
    dice_label.config(text=value)

# 🎯 Button to roll dice
roll_button = tk.Button(root, text="Roll Dice", font=("Helvetica", 18, "bold"),
                        bg="#00ADB5", fg="white", padx=20, pady=10, command=roll_dice)
roll_button.pack()

# 🎯 Exit button
exit_button = tk.Button(root, text="Exit", font=("Helvetica", 14),
                        bg="#FF4C29", fg="white", padx=10, pady=5, command=root.quit)
exit_button.pack(pady=20)

# Run the GUI
root.mainloop()
