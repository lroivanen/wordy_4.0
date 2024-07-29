#program structure
    #intro
    #working_memory
    #functions
        #function 1, select_text -> str:
        #function 2, text_to_list -> list:
        #function 3, building displayed letters
        #function 4, hidden_letter to original_letter
        #function 5, guessed letter dictionary
        #function 7, new_game, command 1
        #function 8, exit_game, command 2
        #function 9, save_game, command 3
        #function 10 max_10_saves
        #funtion 11, load_game, command 4
        #function 12, instructions, command 5
        #function 13, IDKFA, secret cheating code
        #function 14, start_new_game
    #main loop
        #checking is game is won
        #receiving letter/command
        #checking if letter is being guessed
        #checking if command is being used
        #checking if cheat code is being used
        #showing the result of found letter
        #showing result of wrongly guessed letter
        #if wrong command is used
    #comments



#intro
import random
from datetime import datetime

print(" ")
print("Welcome to play:")
print("")
print("")
print(" ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄   ▄         ▄ ")
print("▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░▌       ▐░▌")
print("▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌")
print("▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌")
print("▐░▌   ▄   ▐░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌")
print("▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌")
print("▐░▌ ▐░▌░▌ ▐░▌▐░▌       ▐░▌▐░█▀▀▀▀█░█▀▀ ▐░▌       ▐░▌ ▀▀▀▀█░█▀▀▀▀ ")
print("▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌▐░▌     ▐░▌  ▐░▌       ▐░▌     ▐░▌     ")
print("▐░▌░▌   ▐░▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ")
print("▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░▌      ▐░▌     ")
print(" ▀▀       ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀        ▀      ")
print("The happy word-game :) ")
print(" ")
print("By HyMi-soft")
print("")
print("Please use following commands to play the game:")
print("1. New game            4. Load game")
print("2. Exit game           5. Instructions")
print("3. Save game")
print("")
print("")

#working_memory:

the_list=[]
display=""
guessed_letters={}
guessed_letters_display=""
loaded_games=[]

#functions

#function 1, select_text -> str:

def select_text()->str:
    with open("text.txt") as file:
        lines = file.readlines()
        random_line=random.choice(lines)
    return random_line.strip()

#function 2, text_to_list -> list:

def text_to_list(text: str)->list:
    letter_list=[]
    for i in range(len(text)):
        if text[i].isalpha():
            letter_list.append([text[i],"_ "])
        elif text[i]==" ":
            letter_list.append([text[i]," "])
        else:
            letter_list.append([text[i],"_ "])
    return letter_list

#function 3, building displayed letters:

def display_letters(text_to_list: list)->str:
    display=""
    for original_letter,hidden_letter in text_to_list:
        display+=hidden_letter
    return display

#function 4, hidden_letter to original_letter:

def letter_to_list(letter: str) ->bool:
    found= False
    for item in the_list:
        if item[0] == letter:
            item[1] = letter
            found= True
    return found

#function 5, guessed letter dictionary (dictionary used to avoid duplicates and to meet task requirements)

def update_guessed_letters_display(letter:str):
    global guessed_letters
    global guessed_letters_display
    guessed_letters[letter]=letter
    guessed_letters_display = " ".join(sorted(guessed_letters.keys()))
        

#function 7, new_game, command 1

def new_game():
    global the_list, display, guessed_letters, guessed_letters_display, selected_text
    selected_text = select_text()
    the_list = text_to_list(selected_text)
    display = display_letters(the_list)
    guessed_letters = {}
    guessed_letters_display = ""
    print(f"Guess the sentence: {display}")
#function 8, exit_game, command 2

def exit_game():
    print("Exiting the game.")
    exit()

#function 9, save_game, command 3

def save_game(selected_text, display, guessed_letters_display):
    while True:
        save_title = input("Enter save name: ")
        
        if ";" in save_title:
            print("Please don't use character ';' in the title. It's reserved for internal use.")
        else:
            break  
    
    current_date = datetime.now().strftime("%Y-%m-%d")
    the_row = f"{str(current_date)};{str(save_title)};{str(selected_text)};{str(display)};{str(guessed_letters_display)}\n"
    
    with open("saved_games.txt", "a") as file1:
        file1.write(the_row)
        
    print("Game saved successfully")

#function 10 max_10_saves

def max_10_saves():

    with open("saved_games.txt", "r") as file:
        lines = file.readlines()
    if len(lines) > 10:
        lines = lines[1:]
        with open("saved_games.txt", 'w') as file:
            file.writelines(lines)
        

#funtion 11, load_game, command 4

def load_game():
    global loaded_games, selected_text, display, guessed_letters_display, the_list, guessed_letters
    with open("saved_games.txt") as file:
        counter = 0
        print("Saved games:")
        for row in file:
            if not row or ";" not in row:
                continue
            date1, title1, selected_text1, display1, guessed_letters_display1 = row.strip().split(";")
            counter += 1
            print(f"{counter}. {date1} {title1}")
            loaded_games.append([selected_text1, display1, guessed_letters_display1])
    
    while True:
        try:
            chosen_game = int(input("Choose a game to be loaded (1-10): "))
            if 1 <= chosen_game <= 10:
                break
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a single number.")
    print(" ")
    selected_text2, display2, guessed_letters_display2 = loaded_games[chosen_game - 1]
    
    selected_text = selected_text2
    display = display2
    guessed_letters_display = guessed_letters_display2

    # Recreate the_list based on the selected_text
    the_list = text_to_list(selected_text)
    guessed_letters = {letter: letter for letter in guessed_letters_display.replace(" ", "")}
    for letter in guessed_letters.keys():
        letter_to_list(letter)
    display = display_letters(the_list)
    
    print(f"Loaded game: {display}")
    print(f"You have guessed: {guessed_letters_display}")         

#function 12, instructions, command 5
def instructions():
    print("Guess the given sentence by typing a letter to command line.")
    print("Once all letters have been guessed correctly and whole sentence is revealed, you win the game.")
    print(" ")

#function 13, IDKFA, secret cheating code (jonnet ei muista)

def check_cheat_code(letter_guess):
    if letter_guess.strip().upper() == "IDKFA":
        return True
    return False

#function 14, start_new_game

def start_new_game():
    global the_list, display, guessed_letters, guessed_letters_display, selected_text
    selected_text = select_text()
    the_list = text_to_list(selected_text)
    display = display_letters(the_list)
    guessed_letters = {}
    guessed_letters_display = ""
    print(f"Guess the sentence: {display}")

#main loop

selected_text=select_text()
the_list=text_to_list(selected_text)
display=display_letters(the_list)
print(f"guess the sentence {display}")

while True:

    #checking is game is won
    if display == selected_text:
        print(f"guess the sentence: {display}")
        print(" ")
        print("██    ██  ██████  ██    ██     ██     ██  ██████  ███    ██ ██ ")
        print(" ██  ██  ██    ██ ██    ██     ██     ██ ██    ██ ████   ██ ██ ")
        print("  ████   ██    ██ ██    ██     ██  █  ██ ██    ██ ██ ██  ██ ██ ")
        print("   ██    ██    ██ ██    ██     ██ ███ ██ ██    ██ ██  ██ ██    ")
        print("   ██     ██████   ██████       ███ ███   ██████  ██   ████ ██ ")
        print(" ")
        start_new_game()
        
    #receiving letter/command
    else: 
        letter_guess = input("Give a letter/command: ")
        print(" ")
    #checking if letter is being guessed
        if len(letter_guess)!=1 and not "IDKFA":
            print("Please kindly use only one letter or number as input.")
    #checking if command is being used
        elif letter_guess=="1":
            start_new_game()
        elif letter_guess=="2":
            exit_game()
        elif letter_guess=="3":
            save_game(selected_text, display, guessed_letters_display)
            max_10_saves()
        elif letter_guess=="4":
            load_game()
        elif letter_guess=="5":
            instructions()
    #checking if cheat code is being used
        elif check_cheat_code(letter_guess):
            display=selected_text
            print(f"guess the sentence: {display}")
            print(" ")
            print("██    ██  ██████  ██    ██     ██     ██  ██████  ███    ██ ██ ")
            print(" ██  ██  ██    ██ ██    ██     ██     ██ ██    ██ ████   ██ ██ ")
            print("  ████   ██    ██ ██    ██     ██  █  ██ ██    ██ ██ ██  ██ ██ ")
            print("   ██    ██    ██ ██    ██     ██ ███ ██ ██    ██ ██  ██ ██    ")
            print("   ██     ██████   ██████       ███ ███   ██████  ██   ████ ██ ")
            print(" ")
            start_new_game()
        
    #showing the result of found letter
        elif letter_to_list(letter_guess) and letter_guess.isalpha:
            display = display_letters(the_list)
            print(f"guess the sentence: {display}")
            print(f"letter '{letter_guess}' was found!")
            update_guessed_letters_display(letter_guess)
            print(f"you have guessed: {guessed_letters_display}")

    #showing result of wrongly guessed letter       
        elif letter_guess.isalpha:
            
            print(f"guess the sentence: {display}")
            print("Letter was not found.")
            update_guessed_letters_display(letter_guess)
            print(f"you have guessed: {guessed_letters_display}")
            
    #if wrong command is used        
        else:
            print(f"Command {letter_guess} doesn't exist. Please use commands 1-5.")
       
#comments:

#task requirements:
    #min 5 functions
        #14 funtions used
    #reading and writing from file
        #reading in load_game function
        #writing in save_game function
        #ereasing in max_10_saves function
    #100 lines of code
        #300+ gaps and #comments included
    #use of lists and dictionarys
        #both used in memory 
    #external libraries
        #random
        #datetime
    #documentation/structure
        #original plan (word.file)
        #this commentary
    #solution principle
        #program takes random sentence from a text.txt file
        #for simplicity reasons, all texts consists only spaces and lower case letters
        #sentence is chopped into a list structure that changes characters into hidden letters ("_") and displays them
        #main loop is used to convert hidden letters in display to original letters
        #game is won when displayed text equals the original text
        #memory part is used to store all variables during process

        #when game is saved, "save_game" function takes string variables and saves them into saved game file
        #when game is loaded, "load_game" function reads string form variables from the file and reconstructs list and dict variables

        #other features
            #all inputs are protected with true-false loop or try-exception method
            #max_10_saves function ensures that saved games file wont get too bloated
            #IDKFA cheat code changes the display to original text and wins the game
            #exceptions in inputs for IDKFA have been built to allow code being used, but preventing other "wrong" inputs
            #user experience has been tried to improve various ways

    #UTU ethical guidelines of learning disclaimer
        #chatGPT AI has been used to troubleshoot the code and to get inspiration for some solutions
        #only code that I understand 100% has been included
        #solution principle of "load_game" function had been more influenced by AI than the others
        #texts for the text.txt file have been all generated by AI


