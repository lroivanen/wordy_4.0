#program structure
    #GUI setup
    #functions
        #select_text
        #display_letters
        #letter_to_list
        #update_guessed_letters_display
        #new_game
        #exit_game
        #save_game
        #prompt_save_game
        #load_game
        #show_load_game_popup
        #load_selected_game
        #instructions
        #update_display
        #update_info_text
        #on_enter
    #comments
        


import tkinter as tk
from tkinter import messagebox
import random
from datetime import datetime
from tkinter import simpledialog
from tkinter import Toplevel, Listbox, Scrollbar

class MyGUI:
    def __init__(self):

        # GUI setup
        self.root = tk.Tk()
        self.root.geometry("900x600")
        self.root.title("Wordy!")

        #headline
        self.label = tk.Label(self.root, text="Wordy :)", font=("Arial", 24))
        self.label.pack(padx=20, pady=20)

        #buttons
        buttonframe = tk.Frame(self.root)
        buttonframe.columnconfigure(0, weight=1)
        buttonframe.columnconfigure(1, weight=1)
        buttonframe.columnconfigure(2, weight=1)

        btn1 = tk.Button(buttonframe, text="1. New Game", font=("Arial", 18), command=self.new_game)
        btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

        btn2 = tk.Button(buttonframe, text="2. Exit Game", font=("Arial", 18), command=self.exit_game)
        btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

        btn3 = tk.Button(buttonframe, text="3. Save Game", font=("Arial", 18), command=self.prompt_save_game)
        btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

        btn4 = tk.Button(buttonframe, text="4. Load Game", font=("Arial", 18), command=self.load_game)
        btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

        btn5 = tk.Button(buttonframe, text="5. Instructions", font=("Arial", 18), command=self.instructions)
        btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

        buttonframe.pack(padx=30)

        #instruction label
        self.label = tk.Label(self.root, text="Try to guess this sentence", font=("Arial", 18))
        self.label.pack(padx=20, pady=20)

        #display_label (hidden word display)
        self.display_label = tk.Label(self.root, text="init", font=("Arial", 18))
        self.display_label.pack(padx=20, pady=20)

        self.guess_label = tk.Label(self.root, text="Give me a letter:", font=("Arial", 12))
        self.guess_label.pack(padx=20)

        #entry field
        self.entry = tk.Entry(self.root)
        self.entry.pack()

        #quessed_letters_display box
        self.guessed_letters_display = tk.Label(self.root, text="", font=("Arial", 12))
        self.guessed_letters_display.pack(padx=20)

        #info_text box
        self.info_text = tk.Text(self.root, height=3, font=("Arial", 16))
        self.info_text.pack(padx=30, pady=50)
        self.info_text.insert(tk.END, "Welcome to play Wordy! The happy word game. :)")
        self.info_text.config(state=tk.DISABLED)

        # Game state / "memory"
        self.the_list = []
        self.guessed_letters = {}
        self.loaded_games = []
        self.selected_text = ""

        # Start a new game
        self.new_game()

        self.root.bind('<Return>', self.on_enter)
        self.root.mainloop()

        #select random text from the list
    def select_text(self) -> str:
        with open("text.txt") as file:
            lines = file.readlines()
            random_line = random.choice(lines)
        return random_line.strip()
    
        #creates "the_list" to gamestate section
    def text_to_list(self, text: str) -> list:
        letter_list = []
        for char in text:
            if char.isalpha():
                letter_list.append([char, "_ "])
            elif char == " ":
                letter_list.append([char, " "])
            else:
                letter_list.append([char, "_ "])
        return letter_list

        #creates display for "hidden" letters
    def display_letters(self, text_to_list: list) -> str:
        display = ""
        for original_letter, hidden_letter in text_to_list:
            display += hidden_letter
        return display
    
        #checks if letter is in the sentence
    def letter_to_list(self, letter: str) -> bool:
        found = False
        for item in self.the_list:
            if item[0] == letter:
                item[1] = letter
                found = True
        return found

        #reveals found letters in the display
    def update_guessed_letters_display(self, letter: str):
        if letter in self.guessed_letters:
            return

        self.guessed_letters[letter] = letter
        remaining_letters = sorted(set("abcdefghijklmnopqrstuvwxyz") - set(self.guessed_letters.keys()))
        display_text = " ".join(remaining_letters)
        self.guessed_letters_display.config(text=display_text)

        #resets game state, selects new random texts = new game
    def new_game(self):
        self.selected_text = self.select_text()
        self.the_list = self.text_to_list(self.selected_text)
        display = self.display_letters(self.the_list)
        self.guessed_letters = {}
        self.update_display(display)
        self.update_guessed_letters_display("")
        self.update_info_text("New game started. Good luck!")

        #exit
    def exit_game(self):
        self.root.destroy()

        #saves key values from game state and writes them with date to saved games file
        #also checks that the file doesnt have more than 20 saved games and removes the oldest if needed
    def save_game(self, save_title):
        current_date = datetime.now().strftime("%Y-%m-%d")
        the_row = f"{str(current_date)};{str(save_title)};{str(self.selected_text)};{str(self.display_letters(self.the_list))};{str(' '.join(self.guessed_letters.keys()))}\n"

        saved_games = []
        try:
            with open("saved_games.txt", "r") as file:
                saved_games = file.readlines()
        except FileNotFoundError:
            pass

        if len(saved_games) >= 20:
            saved_games.pop(0) 

        saved_games.append(the_row)

        with open("saved_games.txt", "w") as file:
            file.writelines(saved_games)
        
        self.update_info_text("Game saved successfully")

        #asks name for saved game
    def prompt_save_game(self):
        save_title = simpledialog.askstring("Save Game", "Enter save name:")
        if save_title:
            self.save_game(save_title)

        #reads lines from saved games, rebuilds game state from str values.
    def load_game(self):
        with open("saved_games.txt") as file:
            self.loaded_games = []
            for row in file:
                if not row or ";" not in row:
                    continue
                date1, title1, selected_text1, display1, guessed_letters_display1 = row.strip().split(";")
                self.loaded_games.append([date1, title1, selected_text1, display1, guessed_letters_display1])

        if self.loaded_games:
            self.show_load_game_popup()

        #shows dates and names of saved games in pop-up
    def show_load_game_popup(self):
        load_popup = Toplevel(self.root)
        load_popup.title("Load Game")
        load_popup.geometry("300x300")

        scrollbar = Scrollbar(load_popup)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        listbox = Listbox(load_popup, yscrollcommand=scrollbar.set, font=("Arial", 12))
        for idx, game in enumerate(self.loaded_games):
            listbox.insert(tk.END, f"{game[0]} - {game[1]}")
        listbox.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        scrollbar.config(command=listbox.yview)

        load_button = tk.Button(load_popup, text="Load", font=("Arial", 12), command=lambda: self.load_selected_game(listbox.curselection(), load_popup))
        load_button.pack(pady=10)

        #sets the game state ready to be played
    def load_selected_game(self, selection, popup):
        if not selection:
            return
        idx = selection[0]
        selected_game = self.loaded_games[idx]
        selected_text2, display2, guessed_letters_display2 = selected_game[2], selected_game[3], selected_game[4]
        self.selected_text = selected_text2
        self.the_list = self.text_to_list(self.selected_text)
        self.guessed_letters = {letter: letter for letter in guessed_letters_display2.split()}
        for letter in self.guessed_letters.keys():
            self.letter_to_list(letter)
        self.update_display(display2)
        self.update_guessed_letters_display("")
        self.update_info_text("Game loaded successfully")
        popup.destroy()

        #displays game instructions
    def instructions(self):
        instructions_text =(
            "Guess the given sentence by typing a letter.\n"
            "Once all letters have been guessed correctly and the whole sentence is revealed,\n" 
            "you win the game! :)"
            )
        self.update_info_text(instructions_text)
        
        #updates display
    def update_display(self, text):
        self.display_label.config(text=text)

        #updates info text box
    def update_info_text(self, text):
        self.info_text.config(state=tk.NORMAL)
        self.info_text.delete(1.0, tk.END)
        self.info_text.insert(tk.END, text)
        self.info_text.config(state=tk.DISABLED)

        #on enter method! Core function of the game!
    def on_enter(self, event):
        letter_guess = self.entry.get().strip()
        self.entry.delete(0, tk.END)

        if letter_guess == "IDKFA":
            # jonnet ei muista
            display = self.selected_text
            self.update_display(display)
            messagebox.showinfo("You Win!", f"Congratulations, you guessed the sentence!\n'{display}'")
            self.new_game()
            return
        
        if len(letter_guess) != 1:
            self.update_info_text("Please enter a single letter.")
            return

        if letter_guess.isalpha():
            if self.letter_to_list(letter_guess):
                display = self.display_letters(self.the_list)
                self.update_display(display)
                self.update_guessed_letters_display(letter_guess)
                if display == self.selected_text:
                    messagebox.showinfo("You Win!", f"Congratulations, you guessed the sentence!\n'{display}'")
                    self.new_game()
            else:
                self.update_info_text(f"Letter '{letter_guess}' was not found.")
                self.update_guessed_letters_display(letter_guess)

MyGUI()

#comments:

#task requirements:
    #min 5 functions
        #14 funtions used
    #reading and writing from file
        #reading in load_game function
        #writing in save_game function
        #ereasing in max_20_saves function
    #100 lines of code
        #~200 lines
    #use of lists and dictionarys
        #both used in game state / memory 
    #external libraries
        #random
        #datetime
        #tkinter
    #documentation/structure
        #original plan (word.file)
        #this commentary
    #solution principle
        #program takes random sentence from a text.txt file
        #sentence is chopped into a list structure that changes characters into hidden letters ("_") and displays them
        #game is won when displayed text equals the original text
        #game state part is used to store all variables during process
        #on enter method moves program forward when player presses enter

        #when game is saved, "save_game" function takes string variables and saves them into saved game file
        #when game is loaded, "load_game" function reads string form variables from the file and reconstructs list and dict variables

    #other features
        #all inputs are protected with true-false loop or try-exception method
        #game limits amount of saved games to 20 to avoid too bloated save_game file
        #IDKFA cheat code changes the display to original text and wins the game
        #exceptions in inputs for IDKFA have been built to allow code being used, but preventing other "wrong" inputs
        #GUI

    #UTU ethical guidelines of learning disclaimer
        #chatGPT AI has been used to troubleshoot the code and to get inspiration for some solutions
        #only code that I understand 100% has been included
        #solution principle of "load_game" function had been more influenced by AI than the others
        #texts for the text.txt file have been all generated by AI
    
        #wordy 2.0 with GUI was created with assistance of AI.
        #UI without functionalities was first handwritten.
        #AI was used to "smash" the text based wordy 1.0 and GUI together
        #shortcomings and bugs of the AI generated "smashed" code were manually corrected
        #most notable change done by AI was "on enter" method, that I would not have came up myself