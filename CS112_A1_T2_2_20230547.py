# File: CS112_A1_T2_2_20230547
'''
# Purpose: Number scrabble is played with the list of numbers between 1 and 9. Each player takes
turns picking a number from the list. Once a number has been picked, it cannot be picked
again. If a player has picked three numbers that add up to 15, that player wins the game.
However, if all the numbers are used and no player gets exactly 15, the game is a draw.
'''
# Author: Mohamed Ehab Sabry
# ID: 20230547
# The introductory message, the comments, and some tweakings to the format were done using ChatGPT 3.5, but no actual code was copied or generated.



from itertools import combinations

# Global variables
pl1_name = ''  # Player 1's name
pl2_name = ''  # Player 2's name
Num_list = list(range(1, 10))  # List of available numbers
pl1_choices = []  # Player 1's chosen numbers
pl2_choices = []  # Player 2's chosen numbers
valid_menu_choices = ['1', '2']  # Valid menu choices
choice = 0  # Player's choice
choices_counter = 0  # Counter for choices made
winner = False  # Flag to track if there's a winner
menu_choice = ''  # Menu choice


def menu():
    """
    Displays the game menu and handles user input to start the game or exit.
    """
    global pl1_name, pl2_name, Num_list, pl1_choices, pl2_choices, valid_menu_choices, choice, choices_counter, winner, menu_choice
    # Welcome message and game introduction
    print("\033[94m\033[1m Welcome to Number Scrabble! A game of strategic thinking and clever choices. \033[0m \n")
    print("In Number Scrabble, your goal is to outwit your opponent by selecting numbers strategically.")
    print("Each player takes turns choosing a number from the list of available numbers, ranging from 1 to 9.")
    print("The game continues until one player successfully forms a combination of three numbers that adds up to 15.")
    print("If all numbers are chosen without any player achieving this combination, the game ends in a draw.")
    print("Get ready to engage your mind and enjoy the thrill of Number Scrabble!\n")

    # Menu to start the game or exit
    menu_choice = input("Pick \033[93m\033[1m(1)\033[0m to start the game or \033[93m\033[1m(2)\033[0m to exit: ")

    # Validate menu choice
    while menu_choice not in valid_menu_choices:
        menu_choice = input("\033[91;1mInvalid input\033[0m, please pick \033[93m\033[1m(1)\033[0m to start the game or \033[93m\033[1m(2)\033[0m to exit: ")

    if menu_choice == '1':
        # Input players' names and initialize game variables
        pl1_name = input('Please enter the name of the first contestant: ')
        pl2_name = input('Please enter the name of the second contestant: ')
        Num_list = list(range(1, 10))  # Reset list of available numbers
        pl1_choices = []  # Reset player 1's choices
        pl2_choices = []  # Reset player 2's choices
        choice = 0  # Reset choice variable
        choices_counter = 0  # Reset choices counter
        winner = False  # Reset winner flag
        menu_choice = ''  # Reset menu choice
        main_game()
    elif menu_choice == '2':
        exit()


def main_game():
    """
    Main game loop where players take turns choosing numbers until a winner is found or the game ends in a draw.
    """
    global choices_counter, winner
    # Main game loop
    while choices_counter < 9:
        # Player 1's turn
        correct_choice = 0
        while correct_choice == 0:
            try:
                choice = int(input(f'{pl1_name}, choose a number from this list {Num_list}: '))
                if choice in Num_list:
                    correct_choice = 2
                else:
                    while choice not in Num_list:
                        choice = int(input('\033[91mThe number you have entered is invalid, please choose a number from 1-9: \033[0m'))
                    correct_choice = 2

            except ValueError:
                correct_choice = 1

            while correct_choice == 1:
                try:
                    choice = int(input('\033[91mAll characters except for numbers are not allowed, please choose a number from 1-9: \033[0m'))
                    while choice not in Num_list:
                        choice = int(input('\033[91mThe number you have entered is not valid, please choose a number from 1-9: \033[0m'))
                    correct_choice = 2
                except:
                    continue
        
        pl1_choices.append(choice)
        choices_counter += 1
        Num_list.remove(choice)

        # Check if player 1 has won
        for trio in combinations(pl1_choices, 3):
            if sum(trio) == 15:
                print(f'\nCongratulations \033[92m{pl1_name}\033[0m🥳, You have won the game 💯')
                print(f'Hard Luck \033[91m{pl2_name}\033[0m😞, Better luck next time 😉\n\n\n')
                winner = True
                menu()
                
            elif choices_counter == 9: # If there is no winner, the game ends in a draw
                print("It's a draw gentlemen. Have some rest and try again.")
                menu()

    
        # Player 2's turn
        choice = 0
        correct_choice = 0
        while correct_choice == 0:
            try:
                choice = int(input(f'{pl2_name}, choose a number from this list {Num_list}: '))
                if choice in Num_list:
                    correct_choice = 2
                else:
                    while choice not in Num_list:
                        choice = int(input('\033[91mThe number you have entered is not valid, please choose a number from 1-9: \033[0m'))
                    correct_choice = 2

            except ValueError:
                correct_choice = 1
                    
            while correct_choice == 1:
                try:
                    choice = int(input('\033[91mAll characters except for numbers are not allowed, please choose a number from 1-9: \033[0m'))
                    while choice not in Num_list:
                        choice = int(input('\033[91mThe number you have entered is not valid, please choose a number from 1-9: \033[0m'))
                    correct_choice = 2
                except:
                    continue
        
        pl2_choices.append(choice)
        choices_counter += 1
        Num_list.remove(choice)

        # Check if player 2 has won
        for trio in combinations(pl2_choices, 3):
            if sum(trio) == 15:
                print(f'\nCongratulations \033[92m{pl2_name}\033[0m🥳, You have won the game 💯')
                print(f'Hard Luck \033[91m{pl1_name}\033[0m😞, Better luck next time 😉\n\n\n')
                winner = True
                menu()
            elif choices_counter == 9: # If there is no winner, the game ends in a draw
                print("It's a draw gentlemen. Have some rest and try again.")
                menu()    
    
    

menu()  # Start the game