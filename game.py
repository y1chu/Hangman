import random
import tkinter as tk
from tkinter import messagebox


# Function to get the word from the file words.txt
def get_word():
    with open("words.txt", "r") as f:
        words = f.readlines()
    return random.choice(words).strip()


# Function to check if the letter is in the word
def check_letter(letter):
    global word, word_with_spaces, turns, guessed, word_label, turns_label, photo

    text = ""
    if letter in word:
        for i in range(len(word)):
            if letter == word[i]:
                guessed[i] = letter
    else:
        turns -= 1
        photo = tk.PhotoImage(file="hangman" + str(9 - turns) + ".png")
        photo_label.configure(image=photo)
        photo_label.image = photo

    if turns == 0:
        messagebox.showinfo("DEDGE", "You lost the game, the word was " + "\"" + word + "\".")
        play()

    for i in guessed:
        text += i + " "
    word_label.configure(text=text)

    if word == "".join(guessed):
        messagebox.showinfo("POGGERS", "You won the game! The word is " + "\"" + word + "\".")
        play()

    turns_label.configure(text="Guesses Left: " + str(turns))


# Function to play
def play():
    global word, word_with_spaces, turns, guessed, word_label, turns_label, photo
    word = get_word()
    word_with_spaces = " ".join(word)
    guessed = ["_"] * len(word)
    turns = 9
    word_label.configure(text=" ".join(guessed))
    turns_label.configure(text="Guesses Left: " + str(turns))
    photo = tk.PhotoImage(file="hangman0.png")
    photo_label.configure(image=photo)
    photo_label.image = photo


# function to give hint using the one letter the user has not guessed
def hint():
    global word, word_with_spaces, turns, guessed, word_label, turns_label, photo
    text = ""
    for i in range(len(word)):
        if guessed[i] == "_":
            guessed[i] = word[i]
            break
    for i in guessed:
        text += i + " "
    word_label.configure(text=text)

    # if won, output the message and the word and the definition of the word
    if word == "".join(guessed):
        messagebox.showinfo("POGGERS", "You won the game! The word is " + "\"" + word + "\".")
        play()


# Main function
if __name__ == "__main__":
    word = get_word()
    word_with_spaces = " ".join(word)
    guessed = ["_"] * len(word)
    turns = 9

    window = tk.Tk()
    window.title("Hangman By @y1chu")
    window.geometry("700x700")

    photo = tk.PhotoImage(file="hangman0.png")
    photo_label = tk.Label(image=photo)
    photo_label.pack(pady=(20, 0))

    word_label = tk.Label(text=" ".join(guessed), font=("Helvetica", 24))
    word_label.pack(pady=(20, 0))

    turns_label = tk.Label(text="Guesses Left: " + str(turns), font=("Helvetica", 18))
    turns_label.pack(pady=(20, 0))

    button_frame = tk.Frame(window)
    button_frame.pack()

    for i in range(26):
        button = tk.Button(
            button_frame,
            text=chr(97 + i),
            font=("Helvetica", 18),
            width=4,
            command=lambda x=chr(97 + i): check_letter(x),
        )
        button.grid(row=i // 9, column=i % 9)

    play_button = tk.Button(window, text="New Word!", font=("Helvetica", 18), command=play)
    play_button.pack(pady=(20, 0))

    hint_button = tk.Button(window, text="Hint", font=("Helvetica", 15), command=hint)
    hint_button.pack(pady=(10, 0))

    window.mainloop()
