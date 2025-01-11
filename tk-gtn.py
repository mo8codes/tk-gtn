# Imports
import tkinter
from tkinter import *
import random

# Create the root window
mainframe = tkinter.Tk()

#Classes 
class MyLabel(Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, font=("TrebuchetMS", 20), padx=10, pady=10, bg="#0045FF", fg="white",  **kwargs)


class MyButton(Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, font=("TrebuchetMS", 20), padx=10, pady=10, bg="#0070FF", fg="white",bd=3, **kwargs)  

# Guess The Number
def gtn():
    start_game()
    destroy_main_menu()
    pack_gtn_menu()

# Initialise the random number
def start_game():
    global target_number
    target_number = random.randint(1, 10)

# Pack the widgets for the GTN menu
def pack_gtn_menu():
    global InstructionLabel
    global GuessEntry
    global SubmitButton
    global FeedbackLabel

    InstructionLabel = MyLabel(master=mainmenu, text="Guess a number between 1 and 10")
    GuessEntry = Entry(master=mainmenu)
    SubmitButton = MyButton(master=mainmenu, text="Submit", command=check_guess)
    FeedbackLabel = MyLabel(master=mainmenu, text=" ")

    InstructionLabel.pack()
    GuessEntry.pack()
    SubmitButton.pack()
    FeedbackLabel.pack()

# Check the user's guess
def check_guess():
    # Check if the input is a number
    try:
        user_guess = int(GuessEntry.get())
    except ValueError:
        FeedbackLabel.config(text="Please enter a valid number.")
        return

    # If the user is a number then check if it is between 1-10
    if user_guess < 1 or user_guess > 10:
        FeedbackLabel.config(text="Guess outside of range.")
    
    # Tell the user whether the guess is larger or smaller than the expected number
    elif user_guess < target_number:
        FeedbackLabel.config(text="Guess too small.")
    elif user_guess > target_number:
        FeedbackLabel.config(text="Guess too large.")

    # The user selects the correct number
    else:
        # Tell the user they won and remove the submit guess button
        FeedbackLabel.config(text="Correct! You guessed the number.")
        SubmitButton.destroy()

        # Create the main menu button so they can go back to the main menu
        global MainMenuButton
        MainMenuButton = MyButton(master=mainmenu, text="Main Menu", command=gtn_won)
        MainMenuButton.pack()

# Go back to the main menu
def gtn_won():
    destroy_gtn_menu()
    pack_main_menu()

# Remove the gtn menu widgets
def destroy_gtn_menu():
    InstructionLabel.destroy()
    GuessEntry.destroy()
    FeedbackLabel.destroy()
    MainMenuButton.destroy()
    

#Main Menu
def pack_main_menu():
    global TitleLabel
    global StartButton

    TitleLabel = MyLabel(master=mainmenu, text="Guess the Number")
    TitleLabel.pack()

    StartButton = MyButton(master=mainmenu, text="Start", command=gtn)
    StartButton.pack()

def destroy_main_menu():
    global TitleLabel
    global StartButton

    TitleLabel.destroy()
    StartButton.destroy()


#Initial Window
mainmenu = Frame(master=mainframe, height=400, width=600, bg="#0045FF")
mainmenu.pack(fill=tkinter.BOTH, expand=True)
pack_main_menu()
mainframe.geometry("600x400")
mainframe.title("Guess the Number")
mainframe.mainloop()