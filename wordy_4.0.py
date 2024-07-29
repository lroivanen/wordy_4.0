#program structure
    #imports
    #language setup
    #GUI setup
        #menubar
        #language buttons
        #game title and logo
        #instructions label
        #hidden word display
        #entry field
        #quessed_letters_display box
        #info_text box
    #game functions
        #Game state / "memory"
        #change to english
        #change to spanish
        #change to spanish
        #refresh GUI
        #select text
        #display letters
        #letter to list
        #update guessed letters display
        #new game
        #exit game
        #save game
        #promt save game
        #load game
        #show load game popup
        #load selected game
        #instructions
        #update display
        #update info text
        #on enter
        #show win popup
        
#imports

import tkinter as tk
from tkinter import messagebox
import random
from datetime import datetime
from tkinter import simpledialog
from tkinter import Toplevel, Listbox, Scrollbar
from tkinter import PhotoImage
import pygame
from PIL import Image, ImageTk

class MyGUI:
    def __init__(self):

        #language setup
        self.current_language = 'english'

        self.txt_menubartitle="Menu"
        self.txt_game_title=("Pedro's wordgame")
        self.txt_new_game=("New game")
        self.txt_exit_game=("Exit game")
        self.txt_save_game=("Save game")
        self.txt_load_game=("Load game")
        self.txt_instructions=("Instructions")
        self.txt_try_to_guess=("Try to guess this sentence")
        self.txt_give_me_letter=("Give me a letter:")
        self.txt_welcome_message=("Welcome to play Pedro's happy wordgame!")
        self.txt_new_game_started=("New game started, good luck!")
        self.txt_game_saved_success=("Game saved successfully.")
        self.txt_enter_save_name=("Enter save name")
        self.txt_game_loaded_success=("Game loaded successfully.")
        self.txt_instructions_text=("Guess the given sentence by typing a letter.\n"
            "Once all letters have been guessed correctly and the whole sentence is revealed,\n" 
            "you win the game! :)")
        self.txt_please_enter_single_letter=("Please enter a single letter.")
        self.txt_letter=("Letter")
        self.txt_was_not_found=("was not found.")
        self.txt_you_win=("You win!")
        self.txt_congratulations_you_guessed=("Congratulations, you guessed the sentence!")
    
        # sounds setup
        pygame.mixer.init()
    
        self.incorrect_sound = pygame.mixer.Sound("wrong_letter_sound.wav")
        self.pedro_pedro=pygame.mixer.Sound("pedro_pedro.mp3")


        # GUI setup
        self.root = tk.Tk()
        self.root.geometry("900x700")
        self.root.title(self.txt_game_title)

        #menubar
        self.menubar=tk.Menu(self.root)

        self.filemenu=tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label=self.txt_new_game,command=self.new_game)
        self.filemenu.add_command(label=self.txt_save_game,command=self.prompt_save_game)
        self.filemenu.add_command(label=self.txt_load_game,command=self.load_game)
        self.filemenu.add_command(label=self.txt_instructions,command=self.instructions)
        self.filemenu.add_separator()
        self.filemenu.add_command(label=self.txt_exit_game, command=self.exit_game)

        self.actionmenu=tk.Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade
        self.menubar.add_cascade(menu=self.filemenu, label=self.txt_menubartitle)
        self.root.config(menu=self.menubar)

        
        #language buttons
        flag_frame = tk.Frame(self.root)
        flag_frame.pack(side=tk.TOP, anchor=tk.E, padx=10, pady=10)
        self.flag_english = PhotoImage(file="flag_english.png")
        self.flag_spanish = PhotoImage(file="flag_spanish.png")
        self.flag_finnish = PhotoImage(file="flag_finnish.png")
        self.logo = PhotoImage(file="logo.png")
        btn_english = tk.Button(flag_frame, image=self.flag_english, command=self.change_to_english)
        btn_english.pack(side=tk.LEFT, padx=5)
        btn_spanish = tk.Button(flag_frame, image=self.flag_spanish, command=self.change_to_spanish)
        btn_spanish.pack(side=tk.LEFT, padx=5)
        btn_finnish = tk.Button(flag_frame, image=self.flag_finnish, command=self.change_to_finnish)
        btn_finnish.pack(side=tk.LEFT, padx=5)

       #title and logo (frame)
        title_frame = tk.Frame(self.root)
        title_frame.pack(pady=20)
        # Title label
        self.headline_label = tk.Label(title_frame, text=self.txt_game_title, font=("Arial", 24))
        self.headline_label.pack(side=tk.LEFT, padx=10)
        # Logo label
        self.logo_label = tk.Label(title_frame, image=self.logo)
        self.logo_label.pack(side=tk.LEFT)

        #instruction label
        self.try_label = tk.Label(self.root, text=self.txt_try_to_guess, font=("Arial", 18))
        self.try_label.pack(padx=20, pady=20)

        #hidden word display
        self.display_label = tk.Label(self.root, text="init", font=("Arial", 18))
        self.display_label.pack(padx=20, pady=20)
        self.guess_label = tk.Label(self.root, text=self.txt_give_me_letter, font=("Arial", 12))
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
        self.info_text.insert(tk.END, self.txt_welcome_message)
        self.info_text.config(state=tk.DISABLED)

        #GAME FUNCTIONS

        # Game state / "memory"
        self.the_list = []
        self.guessed_letters = {}
        self.loaded_games = []
        self.selected_text = ""

        # Start a new game
        self.new_game()
        self.root.bind('<Return>', self.on_enter)
        self.root.mainloop()

    def change_to_english(self):
        self.current_language = 'english'
        self.txt_menubartitle="Menu"
        self.txt_game_title=("Pedro's wordgame")
        self.txt_new_game=("New game")
        self.txt_exit_game=("Exit game")
        self.txt_save_game=("Save game")
        self.txt_load_game=("Load game")
        self.txt_instructions=("Instructions")
        self.txt_try_to_guess=("Try to guess this sentence")
        self.txt_give_me_letter=("Give me a letter:")
        self.txt_welcome_message=("Welcome to play Pedro's happy wordgame!")
        self.txt_new_game_started=("New game started, good luck!")
        self.txt_game_saved_success=("Game saved successfully.")
        self.txt_enter_save_name=("Enter save name")
        self.txt_game_loaded_success=("Game loaded successfully.")
        self.txt_instructions_text=("Guess the given sentence by typing a letter.\n"
            "Once all letters have been guessed correctly and the whole sentence is revealed,\n" 
            "you win the game! :)")
        self.txt_please_enter_single_letter=("Please enter a single letter.")
        self.txt_letter=("Letter")
        self.txt_was_not_found=("was not found.")
        self.txt_you_win=("You win!")
        self.txt_congratulations_you_guessed=("Congratulations, you guessed the sentence!")
        self.refresh_gui()

    def change_to_spanish(self):
        self.current_language = 'spanish'
        self.txt_menubartitle="Menú"
        self.txt_game_title = ("Juego de palabras de Pedro")
        self.txt_new_game = ("Nuevo juego")
        self.txt_exit_game = ("Salir del juego")
        self.txt_save_game = ("Guardar juego")
        self.txt_load_game = ("Cargar juego")
        self.txt_instructions = ("Instrucciones")
        self.txt_try_to_guess = ("Intenta adivinar esta oración")
        self.txt_give_me_letter = ("Dame una letra:")
        self.txt_welcome_message = ("¡Bienvenido a jugar el juego feliz de palabras de Pedro!")
        self.txt_new_game_started = ("¡Nuevo juego iniciado, buena suerte!")
        self.txt_game_saved_success = ("Juego guardado exitosamente.")
        self.txt_enter_save_name = ("Introduce el nombre para guardar")
        self.txt_game_loaded_success = ("Juego cargado exitosamente.")
        self.txt_instructions_text = ("Adivina la oración dada escribiendo una letra.\n"
                                    "Una vez que todas las letras se hayan adivinado correctamente y la oración completa se revele,\n"
                                    "¡ganas el juego! :)")
        self.txt_please_enter_single_letter = ("Por favor, ingresa una sola letra.")
        self.txt_letter = ("Letra")
        self.txt_was_not_found = ("no fue encontrada.")
        self.txt_you_win = ("¡Ganaste!")
        self.txt_congratulations_you_guessed = ("¡Felicidades, adivinaste la oración!")
        self.refresh_gui()

    def change_to_finnish(self):
        self.current_language = 'finnish'
        self.txt_menubartitle="Valikko"
        self.txt_game_title = ("Pedron sanapeli")
        self.txt_new_game = ("Uusi peli")
        self.txt_exit_game = ("Poistu pelistä")
        self.txt_save_game = ("Tallenna peli")
        self.txt_load_game = ("Lataa peli")
        self.txt_instructions = ("Ohjeet")
        self.txt_try_to_guess = ("Yritä arvata tämä lause")
        self.txt_give_me_letter = ("Anna minulle kirjain:")
        self.txt_welcome_message = ("Tervetuloa pelaamaan Pedron iloista sanapeliä!")
        self.txt_new_game_started = ("Uusi peli aloitettu, onnea!")
        self.txt_game_saved_success = ("Peli tallennettu onnistuneesti.")
        self.txt_enter_save_name = ("Syötä tallennusnimi")
        self.txt_game_loaded_success = ("Peli ladattu onnistuneesti.")
        self.txt_instructions_text = ("Arvaa annettu lause kirjoittamalla kirjain.\n"
                                    "Kun kaikki kirjaimet on arvattu oikein ja koko lause paljastuu,\n"
                                    "voitat pelin! :)")
        self.txt_please_enter_single_letter = ("Syötä vain yksi kirjain.")
        self.txt_letter = ("Kirjainta")
        self.txt_was_not_found = ("ei löytynyt.")
        self.txt_you_win = ("Voitit!")
        self.txt_congratulations_you_guessed = ("Onnittelut, arvasit lauseen!")
        self.refresh_gui()

    def refresh_gui(self):
        self.new_game()
        self.headline_label.config(text=self.txt_game_title)
        self.guess_label.config(text=self.txt_give_me_letter)
        self.try_label.config(text=self.txt_try_to_guess)
        
        self.filemenu.entryconfig(0, label=self.txt_new_game)
        self.filemenu.entryconfig(1, label=self.txt_save_game)
        self.filemenu.entryconfig(2, label=self.txt_load_game)
        self.filemenu.entryconfig(3, label=self.txt_instructions)
        self.filemenu.entryconfig(5, label=self.txt_exit_game)
        self.menubar.entryconfig(label=self.txt_menubartitle)
        
    def select_text(self) -> str:
        #creates "the_list" to gamestate section
        if self.current_language == 'english':
            filename = "text_english.txt"
        elif self.current_language == 'spanish':
            filename = "text_spanish.txt"
        elif self.current_language == 'finnish':
            filename = "text_finnish.txt"

        with open(filename) as file:
            lines = file.readlines()
            random_line = random.choice(lines)
        return random_line.strip()
    
        
    def text_to_list(self, text: str) -> list:
        #creates display for "hidden" letters
        letter_list = []
        for char in text:
            if char.isalpha():
                letter_list.append([char, "_ "])
            elif char == " ":
                letter_list.append([char, " "])
            else:
                letter_list.append([char, char])
        return letter_list

        
    def display_letters(self, text_to_list: list) -> str:
        display = ""
        for original_letter, hidden_letter in text_to_list:
            display += hidden_letter
        return display
    
    def letter_to_list(self, letter: str) -> bool:
        #reveals found letters in the display
        found = False
        for item in self.the_list:
            if item[0] == letter:
                item[1] = letter
                found = True
        return found

        
    def update_guessed_letters_display(self, letter: str):
        if letter in self.guessed_letters:
            return

        self.guessed_letters[letter] = letter
        remaining_letters = sorted(set("abcdefghijklmnopqrstuvwxyz") - set(self.guessed_letters.keys()))
        display_text = " ".join(remaining_letters)
        self.guessed_letters_display.config(text=display_text)

    def new_game(self):
        self.selected_text = self.select_text()
        self.the_list = self.text_to_list(self.selected_text)
        display = self.display_letters(self.the_list)
        self.guessed_letters = {}
        self.update_display(display)
        self.update_guessed_letters_display("")
        self.update_info_text(self.txt_new_game_started)

        
    def exit_game(self):
        self.root.destroy()

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
        
        self.update_info_text(self.txt_game_saved_success)

    def prompt_save_game(self):
        save_title = simpledialog.askstring(self.txt_save_game, self.txt_enter_save_name)
        if save_title:
            self.save_game(save_title)

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

    def show_load_game_popup(self):
        load_popup = Toplevel(self.root)
        load_popup.title(self.txt_load_game)
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

        
    def load_selected_game(self, selection, popup):
        #sets the game state ready to be played
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
        self.update_info_text(self.txt_game_loaded_success)
        popup.destroy()

    def instructions(self):
        local_instructions_text=self.txt_instructions_text
        self.update_info_text(local_instructions_text)
        
    def update_display(self, text):
        self.display_label.config(text=text)

    def update_info_text(self, text):
        self.info_text.config(state=tk.NORMAL)
        self.info_text.delete(1.0, tk.END)
        self.info_text.insert(tk.END, text)
        self.info_text.config(state=tk.DISABLED)

        
        #ON ENTER, KEY FUNCTION
    def on_enter(self, event):
        letter_guess = self.entry.get().strip()
        self.entry.delete(0, tk.END)

        if letter_guess == "IDKFA":
            # jonnet ei muista
            display = self.selected_text
            self.pedro_pedro.play()
            self.update_display(display)
            self.show_win_popup(display)
            self.new_game()
            return

        if len(letter_guess) != 1:
            self.update_info_text(self.txt_please_enter_single_letter)
            return

        if letter_guess.isalpha():
            if self.letter_to_list(letter_guess):
                display = self.display_letters(self.the_list)
                self.update_display(display)
                self.update_guessed_letters_display(letter_guess)
                
                if display == self.selected_text:
                    self.pedro_pedro.play()
                    self.show_win_popup(display)
                    self.new_game()
            else:
                self.update_info_text(f"{self.txt_letter} '{letter_guess}' {self.txt_was_not_found}")
                self.update_guessed_letters_display(letter_guess)
                self.incorrect_sound.play()  # Play incorrect sound

                
    def show_win_popup(self, display):
        win_popup = Toplevel(self.root)
        win_popup.title(self.txt_you_win)
        popup_width = 600
        popup_height = 500

        main_window_width = self.root.winfo_width()
        main_window_height = self.root.winfo_height()
        x = (main_window_width - popup_width) // 2 +120
        y = (main_window_height - popup_height) // 2
        win_popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

        message_label = tk.Label(win_popup, text=self.txt_congratulations_you_guessed)
        message_label.pack(pady=10)
        sentence_label = tk.Label(win_popup, text=f"'{display}'", font=("Arial", 18, "bold"))
        sentence_label.pack(pady=10)

        gif_label = tk.Label(win_popup)
        gif_label.pack()
        image = Image.open("pedro2.webp")
        frames = []

        try:
            while True:
                frames.append(ImageTk.PhotoImage(image.copy()))
                image.seek(len(frames))
        except EOFError:
            pass

        def update_image(frame_index):
            frame = frames[frame_index]
            gif_label.config(image=frame)
            frame_index = (frame_index + 1) % len(frames)
            win_popup.after(40, update_image, frame_index)

        win_popup.after(0, update_image, 0)

        close_button = tk.Button(win_popup, text="Close", command=win_popup.destroy)
        close_button.pack(pady=10)

MyGUI()