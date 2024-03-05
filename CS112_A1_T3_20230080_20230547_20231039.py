# Program: CypherCalc is a python program that serves many purposes, it has six different functionalites listed below:

# Functionalities:
# 1. Grade Calculator: Converts marks to grades based on predefined thresholds.
# 2. Armstrong Number Checker: Determines if a number is an Armstrong number.
# 3. Pi Calculation: Approximates the value of Pi using Leibniz's formula.
# 4. Caesar Cipher Encryption: Encrypts messages using the Caesar cipher technique.
# 5. Lists Equality Checker: Validates equality of elements in two lists.
# 6. Factors Finder: Identifies all factors of a positive integer.

# Authors: 
#       Ayman Ahmed Abdelsamie: problem 1/6    ID:20230080
#       Gamal Megahed Sayed:    problem 2/3    ID:20231039
#       Mohamed Ehab Sabry:     problem 4/5    ID:20230547

# Version: 1.0
# Date: 26/2/2024



def main_menu():
    """
    Displays the program main_menu and handles user input to start the program or exit.
    """
    # List of valid main_menu choices
    valid_menu_choices = [ '1' , '2' , '3' , '4' , '5' , '6' , '7' ]

    # Welcome message and introduction
    print("\033[1m \"---------------------------------------------------------------------------------\"\033[0m \n")

    print("\033[94m\033[1m \"Welcome to CypherCalc - Your loyal computation and encryption assistant !\"\033[0m \n")

    print("\033[1m \"---------------------------------------------------------------------------------\"\033[0m \n")

    print("CypherCalc is your go-to tool for a wide range of tasks.\nFrom grading marks to checking Armstrong numbers and encrypting messages with the Caesar cipher,\nCypherCalc offers a diverse set of functionalities to aid you in doing differnt projects.")

    print("Simply select a task from the menu to get started, or select ('7') to exit:\n")

    print("1) \033[30;47mGrade Calculator\033[0m          2) \033[30;47mArmstrong Number Checker\033[0m            3) \033[30;47mPi Calculation\033[0m")
    
    print("4) \033[37;40mCaesar Cipher Encryption\033[0m  5) \033[37;40mLists Equality Checker\033[0m              6) \033[37;40mFactors Finder\033[0m\n7) \033[30;47mExit\033[0m")

    menu_choice = input("Simply select a task from the menu above to get started, or select \033[93;1m('7')\033[0m to exit:\n")


    # Validate user input
    while menu_choice not in valid_menu_choices:
        menu_choice = input("\033[91;1mInvalid input\033[0m, please select a task from the menu above to get started, or select \033[93;1m('7')\033[0m to exit:\n")

    # Start the encryption program or exit based on user choice
    if menu_choice == '1':
        grade_calc()
    elif menu_choice == '2':
        armstrong_num_checker()

    elif menu_choice == '3':
        pi_calc()

    elif menu_choice == '4':
        cesar_cipher()

    elif menu_choice == '5':
        equality_checker()

    elif menu_choice == '6':
        factors_finder()

    elif menu_choice == '7':
        exit()


# Programs:
def grade_calc():
    def get_grade(grade):
        if 90 <= grade <= 100:
            return 'A+'
        elif 85 <= grade < 90:
            return 'A'
        elif 80 <= grade < 85:
            return 'B+'
        elif 75 <= grade < 80:
            return 'B'
        elif 70 <= grade < 75:
            return 'C+'
        elif 65 <= grade < 70:
            return 'C'
        elif 60 <= grade < 65:
            return 'D+'
        elif 50 <= grade < 60:
            return 'D'
        elif 0 <= grade < 50:
            return 'F'
        else:
            return 'Invalid Mark'

    # Function to get a float from the user, handling exceptions
    def get_float(message):
        x = False
        while not x:
            try:
                num = float(input(message))
            except ValueError:
                # Handle the exception if the input is not a float
                continue
            x = True
        return num

    # Get a numeric grade from the user
    grade = get_float("Enter your grade\n")

    # Display the corresponding grade
    print(get_grade(grade))


def armstrong_num_checker():
    import math

    # Function to check if a number is an Armstrong number
    def Armstrong(value):
        # Calculate the number of digits in the given value
        digits = int(math.log10(value) + 1)
        sum = 0

        # Iterate through each digit in the number
        for i in str(value):
            # Add the digit raised to the power of the total digits
            sum += int(i) ** digits

        # Check if the sum is equal to the original value
        return sum == value

    # Function to get an integer from the user, handling exceptions
    def get_int(message):
        x = False
        while not x:
            try:
                num = int(input(message))
            except ValueError:
                # Handle the exception if the input is not an integer
                continue
            x = True
        return num

    # Get a number from the user
    number = get_int("Enter a number: ")

    # Check if the number is an Armstrong number and print the result
    if Armstrong(number):
        print("This is an Armstrong number")
    else:
        print("Not an Armstrong number")


def pi_calc():
    # Function to get an integer from the user, handling exceptions
    def get_int(message=""):
        x = False
        while not x:
            try:
                num = int(input(message))
            except ValueError:
                # Handle the exception if the input is not an integer
                continue
            x = True
        return num

    # Function to estimate the value of Pi using the Leibniz formula
    def pi(frequency):
        pi_over_4 = 0
        x = 1
        for i in range(0, frequency):
            if i % 2 == 0:
                pi_over_4 += 1 / x
                x += 2
            else:
                pi_over_4 -= 1 / x
                x += 2
        return pi_over_4 * 4

    # Get the number of iterations from the user
    n = get_int("Enter a number\n")

    # Print the estimated value of Pi
    print("Pi = ", pi(n))


def cesar_cipher():
    menu_ces()


def menu_ces():
    """
    Displays the program menu and handles user input to start the program or exit.
    """
    # List of valid menu choices
    valid_menu_choices = ['1', '2']

    # Welcome message and introduction
    print("\033[94m\033[1m \"Welcome! This program is designed to help you encrypt messages using the Caesar cipher, a simple but effective technique for data security\"\033[0m \n")

    # Prompt user to pick an option
    menu_choice = input("Pick \033[93m\033[1m(1)\033[0m to start the program, \033[93m\033[1m(2)\033[0m to return to the main menu or \033[93;1m(3)\033[0m to exit: ")


    # Validate user input
    while menu_choice not in valid_menu_choices:
        menu_choice = input("\033[91;1mInvalid input\033[0m, please pick \033[93m\033[1m(1)\033[0m to start the program, \033[93m\033[1m(2)\033[0m to return to the main menu or \033[93;1m(3)\033[0m to exit: ")

    # Start the encryption program or exit based on user choice
    if menu_choice == '1':
        encryption_prog()
    elif menu_choice == '2':
        return
    elif menu_choice == '3':
        exit()
    

def encryption_prog():
    """
    Encrypts the user-provided message using the Caesar cipher.
    """
    # Prompt user for message to encrypt
    message = input("Enter the message you want to encrypt: ")
    encrypted_message = list(message)  # Convert message to list for manipulation
    num_of_shifts = 1  # Define number of shifts for Caesar cipher
    counter = 0  # Initialize a counter for tracking characters

    # Iterate through each character in the message
    for character2 in range(len(encrypted_message)):
        # If character is 'z', wrap around to 'a'
        if encrypted_message[character2] == 'z':
            encrypted_message[character2] = 'a'
            counter += 1
        # If character is outside alphabet range, skip
        elif 65 > ord(encrypted_message[character2]) or 97 > ord(encrypted_message[character2]) > 90 or ord(encrypted_message[character2]) > 122:
            counter += 1
        # If character is 'Z', wrap around to 'A'
        elif encrypted_message[character2] == 'Z':
            encrypted_message[character2] = 'A'
            counter += 1
        # Encrypt the character using Caesar cipher
        else:
            character_order = ord(message[counter]) + num_of_shifts
            encrypted_message[character2] = chr(character_order)
            counter += 1

    # Convert the encrypted message list back to a string
    encrypted_message_string = "".join(encrypted_message) 
    # Print the original message and the encrypted message
    print(f"Your message is: {message}\nYour encrypted message is: {encrypted_message_string}")


def equality_checker():
    menu_eq()


def menu_eq():
    """
    Displays the program menu and handles user input to start the program or exit.
    """
    # List of valid menu choices
    valid_menu_choices = ['1', '2']

    # Welcome message and introduction
    print("\033[94m\033[1m \"Welcome! This program is designed to help you check the equality of 2 lists contaning integers\"\033[0m \n")

    # Prompt user to pick an option
    menu_choice = input("Pick \033[93m\033[1m(1)\033[0m to start the program, \033[93m\033[1m(2)\033[0m to return to the main menu or \033[93;1m(3)\033[0m to exit: ")

    # Validate user input
    while menu_choice not in valid_menu_choices:
        menu_choice = input("\033[91;1mInvalid input\033[0m, please pick \033[93m\033[1m(1)\033[0m to start the program, \033[93m\033[1m(2)\033[0m to return to the main menu or \033[93;1m(3)\033[0m to exit: ")

    # Start the check equality program or exit based on user choice
    if menu_choice == '1':
        check_equality()
    elif menu_choice == '2':
        return
    elif menu_choice == '3':
        exit()


def check_equality():
    """Checks if two lists have the same integers with the same count for each integer."""

    # Variables and lists  
    first_list = []  # Create an empty list to store the first list elements
    second_list = []  # Create an empty list to store the second list elements
    true_list1 = [] 
    true_list2 = []
    second_list_char_count = [] 
    first_list_char_count = []
    first_list_length = -1
    second_list_length = -1
    number1 = False
    number2 = False
    integer1 = False
    integer2 = False

    while not number1 or first_list_length < 0:
        try:
            first_list_length = int(input("Enter the length of the first list: "))
            number1 = True  # Exit loop if input is valid
        except:
            continue  # Retry if input is invalid

    for object1 in range(first_list_length):
        while not integer1:
            try:
                first_list.append(int(input(f"Enter element number {object1 + 1}: ")))
                integer1 = True  # Exit loop if input is valid
            except:
                continue  # Retry if input is invalid
        integer1 = False  # Reset for the next element

    while not number2 or second_list_length < 0:  # Same logic as above for the second list
        try:
            second_list_length = int(input("Enter the length of the second list: "))
            number2 = True
        except:
            continue

    for object2 in range(second_list_length):
        while not integer2:
            try:
                second_list.append(int(input(f"Enter element number {object2 + 1}: ")))
                integer2 = True
            except:
                continue
        integer2 = False

    # Calculate character counts for the first list
    for char1 in first_list:
        first_list_char_count.append((char1, first_list.count(char1))) 

    # Calculate character counts for the second list
    for char2 in second_list:
        second_list_char_count.append((char2, second_list.count(char2))) 

    # Equality check (iterates over character counts)
    for char3 in first_list_char_count: 
        if char3 in second_list_char_count:
            equal1 = True
            true_list1.append(equal1)
        else:
            equal1 = False
            true_list1.append(equal1)

    for char4 in second_list_char_count:
        if char4 in first_list_char_count:
            equal2 = True
            true_list2.append(equal2)
        else:
            equal2 = False
            true_list2.append(equal2)

    # Final equality determination
    if first_list_length != second_list_length or False in true_list1 or False in true_list2:
        print("Lists are equal = False")
    else:
        print("Lists are equal = True")



def factors_finder():

    def main_program():

# An empty list to add the factors in it
        factors_list = []

    # Welcome message
        print("Welcome to number's factors calculator program😊❤️")

    # Get a positive integer
        validity = True
        while validity:
            try:
                n = int(input('please enter a positive integer '))
                validity = False
            except:
                continue

    # Check if the number is positive
        while n <= 0:
            n = int(input('please enter a positive integer '))

        for i in range(1 , n + 1):
            if n % i == 0:
                factors_list.append(i)
            else:
                continue
        print(f'\033[32m The factor(s) of {n} is(are) {factors_list}\033[0m\n')
        
        again()

    # Menu to check if the user wants to start again
    def again():
        valid_choice = ['A' , 'B']
        choice = input('Do you want to start again?\n A) Yes\n B) No\n').upper()
        while choice not in valid_choice:
            choice = input('\033[91m\033[1m INVALID INPUT\033[0m\n Do you want to start again?\n A) Yes\n B) No\n').upper()
        if choice == 'A':
            main_program()
        elif choice == 'B':
            return


    main_program()


while True:
    main_menu()