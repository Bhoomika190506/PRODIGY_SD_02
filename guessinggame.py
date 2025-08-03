import tkinter as tk
from tkinter import messagebox
import random

secret_number = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts, secret_number

    guess = entry_guess.get().strip()
    if not guess.isdigit():
        messagebox.showerror("Invalid Input", "Please enter a valid number between 1 and 100.")
        return

    guess = int(guess)
    if not 1 <= guess <= 100:
        messagebox.showwarning("Out of Range", "Number must be between 1 and 100.")
        return

    attempts += 1

    if guess < secret_number:
        feedback.set("Too Low! Try again.")
    elif guess > secret_number:
        feedback.set("Too High! Try again.")
    else:
        feedback.set(f"🎉 Correct! You guessed it in {attempts} attempts.")
        btn_check.config(state="disabled")
        entry_guess.config(state="disabled")
        btn_restart.pack(pady=10)

def restart_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    feedback.set("")
    entry_guess.config(state="normal")
    btn_check.config(state="normal")
    entry_guess.delete(0, tk.END)
    btn_restart.pack_forget()

root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("350x270")
root.resizable(False, False)
root.configure(bg="white")

tk.Label(root, text="Guess the Number (1 to 100)", font=("Arial", 12), bg="white").pack(pady=(15, 5))

entry_guess = tk.Entry(root, width=15)
entry_guess.pack(pady=5)
entry_guess.focus()

btn_check = tk.Button(root, text="Check", width=10, command=check_guess)
btn_check.pack(pady=5)

feedback = tk.StringVar()
tk.Label(root, textvariable=feedback, fg="blue", font=("Arial", 11), bg="white").pack(pady=10)

btn_restart = tk.Button(root, text="Play Again", width=10, command=restart_game)

root.bind("<Return>", lambda event: check_guess())

root.mainloop()
