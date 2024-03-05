# Program: Game1 (Connect 4) It's a game where a board of 7 columns x 6 rows is displayed that is held up in physical game.
#          Players choose a symbol, either X or O. In their turn, they drop the symbol from top of the
#          board (number 6) until it settles in the bottom empty cell.
#          The first player to connect 4 symbols horizontally, vertically or diagonally wins. Have fun playing!

# Author: Mohamed Ehab Sabry
# Section: NA
# ID: 20230547
# Version: 1.0
# Date: 19/2/2024




# Libraries
import numpy as np  # Importing NumPy for array manipulation
import os  # Importing os module for system-specific operations
import time as t  # Importing time module for time-related functions

# Variables
rows = 0  # Variable to store the number of rows in the game board (initialized to 0)
colmuns = 7  # Variable to store the number of columns in the game board (initialized to 7)
character = '▒'  # Character representing an empty cell on the game board
bg_yellow = '\033[103m'  # ANSI escape code for yellow background color
bg_reset = '\033[0m'  # ANSI escape code to reset text formatting
game_board = np.full((6, 7), character)  # Initializing the game board as a 6x7 grid filled with empty cells

# Functions

def menu():
    """
    Displays the game menu and handles user input to start the game or exit.
    """
    global pl1_name, pl2_name, valid_menu_choices, menu_choice, rows, colmuns, bg_reset, bg_yellow, game_board

    valid_menu_choices = ['1', '2']  # Valid choices for the game menu

    # Welcome message and game introduction
    print("\n\033[94m\033[1mWelcome to Connect 4!\033[0m\n")
    print("In Connect 4, players take turns dropping colored discs from the top into a grid.")
    print("The discs fall straight down, occupying the lowest available space within the column.")
    print("The objective is to be the first to form a horizontal, vertical, or diagonal line of four of one's own discs.")
    print("Get ready to challenge your opponent and enjoy the game!\n")

    # Menu to start the game or exit
    menu_choice = input("Pick \033[93m\033[1m(1)\033[0m to start the game or \033[93m\033[1m(2)\033[0m to exit: ")

    # Validate menu choice
    while menu_choice not in valid_menu_choices:
        menu_choice = input("\033[91;1mInvalid input\033[0m, please pick \033[93m\033[1m(1)\033[0m to start the game or \033[93m\033[1m(2)\033[0m to exit: ")

    if menu_choice == '1':
        # Input players' names and initialize game variables
        pl1_name = input('Please enter the name of the first contestant: ')
        pl2_name = input('Please enter the name of the second contestant: ')
        rows = 0
        colmuns = 7
        character = '▒'
        bg_yellow = '\033[103m'
        bg_reset = '\033[0m'
        game_board = np.full((6, 7), character)

        main_game()

    elif menu_choice == '2':
        exit()

# Function to check for a win in the horizontal direction
def check_win_hor(grid, row, col, color, player):
    for direction in [-1, 1]:
        count = 0
        for c in range(col, col + direction * 4, direction):
            if c < 0 or c >= len(grid[0]):
                break
            if grid[row][c] == color:
                count += 1
            else:
                break
            if count >= 4:
                print(f"{player} have won horizontally")
                menu()
    return False

# Function to check for a win in the vertical direction
def check_win_ver(grid, row, col, color, player):
    for direction in [-1, 1]:
        count = 0
        for r in range(row, row + direction * 4, direction):
            if r < 0 or r >= len(grid):
                break
            if grid[r][col] == color:
                count += 1
            else:
                break
            if count >= 4:
                print(f"{player} have won vertically")
                menu()
    return False

# Function to check for a win in the diagonal direction
def check_win_diagonal(grid, row, col, color, player):
    for direction_r in [-1, 1]:
        for direction_c in [-1, 1]:
            count = 0
            for way in range(4):
                r = row + way * direction_r
                c = col + way * direction_c
                if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                    break
                if grid[r][c] == color:
                    count += 1
                else:
                    break
            if count >= 4:
                print(f"{player} have won diagonally")
                menu()
    return False

# Function to create and display the game board
def board_creation():
    global game_board
    # Game board creation
    rows_num = 1
    for rows in game_board:
        print(rows_num, f"{bg_yellow}{rows}{bg_reset}")
        rows_num += 1
    print(" ", " ", 1, " ", 2, " ", 3, " ", 4, " ", 5, " ", 6, " ", 7)
    return game_board

def main_game():
    # Variables to track the height of each column and the number of moves made in each column
    column1 = 5
    column2 = 5
    column3 = 5
    column4 = 5
    column5 = 5
    column6 = 5
    column7 = 5
    col1_counter = 0
    col2_counter = 0
    col3_counter = 0
    col4_counter = 0
    col5_counter = 0
    col6_counter = 0
    col7_counter = 0
    valid_col = [1, 2, 3, 4, 5, 6, 7]  # List of valid column choices
    global game_board
    
    # Displaying the initial game board
    board_creation()
    
    correct_1 = False  # Flag to indicate if player 1's input is correct
    correct_2 = False  # Flag to indicate if player 2's input is correct
    
    # Main game loop
    while True:
        while not correct_1:
            try:
                # Player 1's turn
                player1_choice = int(input(f"{pl1_name}, it's your turn, pick the column where you want to place your piece: "))
                if not (0 < player1_choice <= 7) or player1_choice not in valid_col:
                    continue
                correct_1 = True
            except:
                continue
        correct_1 = False

        # Placing player 1's piece based on their choice of column
        if player1_choice == 1:
            # Player 1's choice is column 1
            for anim in range(column1):
                game_board[anim, player1_choice - 1] = 'x'
                board_creation() 
                game_board[anim, player1_choice - 1] = '▒'
                t.sleep(0.2)
                os.system('cls' if os.name == 'nt' else 'clear')
                board_creation()
            game_board[column1, player1_choice - 1] = 'x'
            os.system('cls' if os.name == 'nt' else 'clear')
            board_creation()
            check_win_hor(game_board, column1, (player1_choice - 1), 'x', pl1_name)
            check_win_ver(game_board, column1, (player1_choice - 1), 'x', pl1_name)
            check_win_diagonal(game_board, column1, (player1_choice - 1), 'x', pl1_name)
            column1 -= 1
            col1_counter += 1
            if col1_counter == 6:
                valid_col.remove(1)

        elif player1_choice == 2:
            # Player 1's choice is column 2
            for anim in range(column2):
                game_board[anim, player1_choice - 1] = 'x'
                board_creation() 
                game_board[anim, player1_choice - 1] = '▒'
                t.sleep(0.2)
                os.system('cls' if os.name == 'nt' else 'clear')
                board_creation()
            game_board[column2, player1_choice - 1] = 'x'
            os.system('cls' if os.name == 'nt' else 'clear')
            board_creation()
            check_win_hor(game_board, column2, (player1_choice - 1), 'x', pl1_name)
            check_win_ver(game_board, column2, (player1_choice - 1), 'x', pl1_name)
            check_win_diagonal(game_board, column2, (player1_choice - 1), 'x', pl1_name)
            column2 -= 1
            col2_counter += 1
            if col2_counter == 6:
                valid_col.remove(2)

        elif player1_choice == 3:
            # Player 1's choice is column 3
            for anim in range(column3):
                game_board[anim, player1_choice - 1] = 'x'
                board_creation() 
                game_board[anim, player1_choice - 1] = '▒'
                t.sleep(0.2)
                os.system('cls' if os.name == 'nt' else 'clear')
                board_creation()
            game_board[column3, player1_choice - 1] = 'x'
            os.system('cls' if os.name == 'nt' else 'clear')
            board_creation()
            check_win_hor(game_board, column3, (player1_choice - 1), 'x', pl1_name)
            check_win_ver(game_board, column3, (player1_choice - 1), 'x', pl1_name)
            check_win_diagonal(game_board, column3, (player1_choice - 1), 'x', pl1_name)
            column3 -= 1
            col3_counter += 1
            if col3_counter == 6:
                valid_col.remove(3)

        elif player1_choice == 4:
            # Player 1's choice is column 4
            for anim in range(column4):
                game_board[anim, player1_choice - 1] = 'x'
                board_creation() 
                game_board[anim, player1_choice - 1] = '▒'
                t.sleep(0.2)
                os.system('cls' if os.name == 'nt' else 'clear')
                board_creation()
            game_board[column4, player1_choice - 1] = 'x'
            os.system('cls' if os.name == 'nt' else 'clear')
            board_creation()
            check_win_hor(game_board, column4, (player1_choice - 1), 'x', pl1_name)
            check_win_ver(game_board, column4, (player1_choice - 1), 'x', pl1_name)
            check_win_diagonal(game_board, column4, (player1_choice - 1), 'x', pl1_name)
            column4 -= 1
            col4_counter += 1
            if col4_counter == 6:
                valid_col.remove(4)

        elif player1_choice == 5:
            # Player 1's choice is column 5
            for anim in range(column5):
                game_board[anim, player1_choice - 1] = 'x'
                board_creation() 
                game_board[anim, player1_choice - 1] = '▒'
                t.sleep(0.2)
                os.system('cls' if os.name == 'nt' else 'clear')
                board_creation()
            game_board[column5, player1_choice - 1] = 'x'
            os.system('cls' if os.name == 'nt' else 'clear')
            board_creation()
            check_win_hor(game_board, column5, (player1_choice - 1), 'x', pl1_name)
            check_win_ver(game_board, column5, (player1_choice - 1), 'x', pl1_name)
            check_win_diagonal(game_board, column5, (player1_choice - 1), 'x', pl1_name)
            column5 -= 1
            col5_counter += 1
            if col5_counter == 6:
                valid_col.remove(5)

        elif player1_choice == 6:
            # Player 1's choice is column 6
            for anim in range(column6):
                game_board[anim, player1_choice - 1] = 'x'
                board_creation() 
                game_board[anim, player1_choice - 1] = '▒'
                t.sleep(0.2)
                os.system('cls' if os.name == 'nt' else 'clear')
                board_creation()
            game_board[column6, player1_choice - 1] = 'x'
            os.system('cls' if os.name == 'nt' else 'clear')
            board_creation()
            check_win_hor(game_board, column6, (player1_choice - 1), 'x', pl1_name)
            check_win_ver(game_board, column6, (player1_choice - 1), 'x', pl1_name)
            check_win_diagonal(game_board, column6, (player1_choice - 1), 'x', pl1_name)
            column6 -= 1
            col6_counter += 1
            if col6_counter == 6:
                valid_col.remove(6)


        elif player1_choice == 7:
            # Player 1's choice is column 7
            for anim in range(column7):
                game_board[anim, player1_choice - 1] = 'x'
                board_creation() 
                game_board[anim, player1_choice - 1] = '▒'
                t.sleep(0.2)
                os.system('cls' if os.name == 'nt' else 'clear')
                board_creation()
            game_board[column7, player1_choice - 1] = 'x'
            os.system('cls' if os.name == 'nt' else 'clear')
            board_creation()
            check_win_hor(game_board, column7, (player1_choice - 1), 'x', pl1_name)
            check_win_ver(game_board, column7, (player1_choice - 1), 'x', pl1_name)
            check_win_diagonal(game_board, column7, (player1_choice - 1), 'x', pl1_name)
            column7 -= 1
            col7_counter += 1
            if col7_counter == 6:
                valid_col.remove(7)
    
        # Player 2:
        while not correct_2:
            try:
                player2_choice = int(input(f"{pl2_name}, it's your turn, pick the column where you want to place your piece: "))
                if 0 >= player2_choice or player2_choice > 7:
                    continue
                correct_2 = True
            except:
                continue
        correct_2 = False
        
        if player2_choice == 1:
            # Player 2's choice is column 1
            for anim in range(column1):
                game_board[anim, player2_choice - 1] = 'o'
                board_creation() 
                game_board[anim, player2_choice - 1] = '▒'
                t.sleep(0.2)
                os.system('cls' if os.name == 'nt' else 'clear')
                board_creation()
            game_board[column1, player2_choice - 1] = 'o'
            os.system('cls' if os.name == 'nt' else 'clear')
            board_creation()
            check_win_hor(game_board, column1, (player2_choice - 1), 'o', pl2_name)
            check_win_ver(game_board, column1, (player2_choice - 1), 'o', pl2_name)
            check_win_diagonal(game_board, column1, (player2_choice - 1), 'o', pl2_name)
            column1 -= 1
            col1_counter += 1
            if col1_counter == 6:
                valid_col.remove(1)

        elif player2_choice == 2:
            # Player 2's choice is column 2
            for anim in range(column2):
                game_board[anim, player2_choice - 1] = 'o'
                board_creation() 
                game_board[anim, player2_choice - 1] = '▒'
                t.sleep(0.2)
                os.system('cls' if os.name == 'nt' else 'clear')
                board_creation()
            game_board[column2, player2_choice - 1] = 'o'
            os.system('cls' if os.name == 'nt' else 'clear')
            board_creation()
            check_win_hor(game_board, column2, (player2_choice - 1), 'o', pl2_name)
            check_win_ver(game_board, column2, (player2_choice - 1), 'o', pl2_name)
            check_win_diagonal(game_board, column2, (player2_choice - 1), 'o', pl2_name)
            column2 -= 1
            col2_counter += 1
            if col2_counter == 6:
                valid_col.remove(2)
        
        elif player2_choice == 3:
            # Player 2's choice is column 3
            for anim in range(column3):
                game_board[anim, player2_choice - 1] = 'o'
                board_creation() 
                game_board[anim, player2_choice - 1] = '▒'
                t.sleep(0.2)
                os.system('cls' if os.name == 'nt' else 'clear')
                board_creation()
            game_board[column3, player2_choice - 1] = 'o'
            os.system('cls' if os.name == 'nt' else 'clear')
            board_creation()
            check_win_hor(game_board, column3, (player2_choice - 1), 'o', pl2_name)
            check_win_ver(game_board, column3, (player2_choice - 1), 'o', pl2_name)
            check_win_diagonal(game_board, column3, (player2_choice - 1), 'o', pl2_name)
            column3 -= 1
            col3_counter += 1
            if col3_counter == 6:
                valid_col.remove(3)

        elif player2_choice == 4:
            # Player 2's choice is column 4
            for anim in range(column4):
                game_board[anim, player2_choice - 1] = 'o'
                board_creation() 
                game_board[anim, player2_choice - 1] = '▒'
                t.sleep(0.2)
                os.system('cls' if os.name == 'nt' else 'clear')
                board_creation()
            game_board[column4, player2_choice - 1] = 'o'
            os.system('cls' if os.name == 'nt' else 'clear')
            board_creation()
            check_win_hor(game_board, column4, (player2_choice - 1), 'o', pl2_name)
            check_win_ver(game_board, column4, (player2_choice - 1), 'o', pl2_name)
            check_win_diagonal(game_board, column4, (player2_choice - 1), 'o', pl2_name)
            column4 -= 1
            col4_counter += 1
            if col4_counter == 6:
                valid_col.remove(4)

        elif player2_choice == 5:
            # Player 2's choice is column 5
            for anim in range(column5):
                game_board[anim, player2_choice - 1] = 'o'
                board_creation() 
                game_board[anim, player2_choice - 1] = '▒'
                t.sleep(0.2)
                os.system('cls' if os.name == 'nt' else 'clear')
                board_creation()
            game_board[column5, player2_choice - 1] = 'o'
            os.system('cls' if os.name == 'nt' else 'clear')
            board_creation()
            check_win_hor(game_board, column5, (player2_choice - 1), 'o', pl2_name)
            check_win_ver(game_board, column5, (player2_choice - 1), 'o', pl2_name)
            check_win_diagonal(game_board, column5, (player2_choice - 1), 'o', pl2_name)
            column5 -= 1
            col5_counter += 1
            if col5_counter == 6:
                valid_col.remove(5)

        elif player2_choice == 6:
            # Player 2's choice is column 6
            for anim in range(column6):
                game_board[anim, player2_choice - 1] = 'o'
                board_creation() 
                game_board[anim, player2_choice - 1] = '▒'
                t.sleep(0.2)
                os.system('cls' if os.name == 'nt' else 'clear')
                board_creation()
            game_board[column6, player2_choice - 1] = 'o'
            os.system('cls' if os.name == 'nt' else 'clear')
            board_creation()
            check_win_hor(game_board, column6, (player2_choice - 1), 'o', pl2_name)
            check_win_ver(game_board, column6, (player2_choice - 1), 'o', pl2_name)
            check_win_diagonal(game_board, column6, (player2_choice - 1), 'o', pl2_name)
            column6 -= 1
            col6_counter += 1
            if col6_counter == 6:
                valid_col.remove(6)

        elif player2_choice == 7:
            # Player 2's choice is column 7
            for anim in range(column7):
                game_board[anim, player2_choice - 1] = 'o'
                board_creation() 
                game_board[anim, player2_choice - 1] = '▒'
                t.sleep(0.2)
                os.system('cls' if os.name == 'nt' else 'clear')
                board_creation()
            game_board[column7, player2_choice - 1] = 'o'
            os.system('cls' if os.name == 'nt' else 'clear')
            board_creation()
            check_win_hor(game_board, column7, (player2_choice - 1), 'o', pl2_name)
            check_win_ver(game_board, column7, (player2_choice - 1), 'o', pl2_name)
            check_win_diagonal(game_board, column7, (player2_choice - 1), 'o', pl2_name)
            column7 -= 1
            col7_counter += 1
            if col7_counter == 6:
                valid_col.remove(7)

        # Checking for draw
        if all(count >= 6 for count in [col1_counter, col2_counter, col3_counter, col4_counter, col5_counter, col6_counter, col7_counter]):
            print("It's a draw, better luck next time")
            menu()

menu()
main_game()