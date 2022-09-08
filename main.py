# Imports
import random
import os

# Game function (Spanish)
def game_es():
    rand = random.randint(1, 10) # Number generated when "game_es" is called
    playerInput = input("\033[0;36;40mSeleccioná un número entre 1 y 10: \033[0;34;40m") # Player input
    if playerInput.isnumeric():
        value = int(playerInput)
        if value >= 1 and value <= 10: # If the number is between 1-10
            if value == rand: # If we guessed the number
                print("\033[0;32;40mAdivinaste.")
            else: # If we didn't guess
                print("\033[1;31;40mIncorrecto, el número era " + str(rand) + ".")
        else: # If the number is not between 1-10
            print("\033[0;31;40mEl número ingresado debe estar entre 1 y 10.")
    else:
        print("\033[0;31;40mEl valor ingresado solo puede contener números.")

    game_es() # Restart

# Game function (English)
def game_us():
    rand = random.randint(1, 10) # Number generated when "game_us" is called
    playerInput = input("\033[0;36;40mSelect a number between 1 and 10: \033[0;34;40m") # Player input
    if playerInput.isnumeric():
        value = int(playerInput)
        if value >= 1 and value <= 10: # If the number is between 1-10
            if value == rand: # If we guessed the number
                print("\033[0;32;40mYou guessed it.")
            else: # If we didn't guess
                print("\033[1;31;40mIncorrect, the number was " + str(rand) + ".")
        else: # If the number is not between 1-10
            print("\033[0;31;40mThe number must be between 1 and 10.")
    else:
        print("\033[0;31;40mThe entered value can only contain numbers.")

    game_us() # Restart

# Language selection
def main():
    print("\033[0;32;40m1 = Spanish")
    print("\033[0;32;40m2 = English")
    playerInput = input("\033[0;36;40mSelect a language (1/2): \033[0;34;40m") # Player input
    if playerInput.isnumeric():
        value = int(playerInput)
        if value >= 1 and value <= 2: # If the number is between 1 and 2
            if value == 1:
                os.system("cls") # Clear the terminal
                game_es() # Start game (Spanish)
            if value == 2:
                os.system("cls") # Clear the terminal
                game_us() # Start game (English)
        else: # If the number is not 1 or 2
            os.system("cls") # Clear the terminal
            print("\033[0;31;40mThat option doesn't exist.")
            main()
    else:
        os.system("cls") # Clear the terminal
        print("\033[0;31;40mThe value entered must be numeric.")
        main()

# Clear the terminal
os.system("cls")

# Start language selection on startup
main()