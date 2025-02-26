import random  # Importing the random module to generate random numbers

# Importing the list of words for Hangman from a separate file
from Hangman_words import words as w

# Function to print instructions for the game
def print_instructions():
    print("Welcome to Hangman!")
    print("The rules are simple:")
    print("1. You will either guess a letter or input a word.")
    print("2. You have a limited number of tries.")
    print("3. Guess the word before you run out of tries!")
    print("Let's start the game!\n")


# Function to select a valid word (without hyphens or spaces) randomly from the list of words
def get_valid_word(w):
    word = random.choice(w)  # Randomly choose a word from the list

    # Ensure the word doesn't contain "-" or spaces
    while "-" in word or " " in word:
        word = random.choice(w)

    return word.upper()  # Return the word in uppercase


# Initialize the scores for the player and the computer
wins_player = 0
wins_comp = 0

# Function for the player to play the Hangman game
def hangman_player():
    chosen_word = get_valid_word(w)  # Get a valid word from the list
    number_of_tries = 0
    letters_of_the_word = list(chosen_word)  # List of letters in the word
    letters_guessed = ""  # Store the letters guessed by the player
    number_of_letters = len(chosen_word)  # Number of letters in the word

    guessing_result = number_of_letters * "_"  # Create the initial guessing result (e.g. _ _ _)

    # Ask the player how many tries they want
    while True:
        try:
            tries = int(input("How many tries do you want : "))  # Get number of tries
            break

        except ValueError:
            print("Not a number!")  # Handle invalid input

    # Start the guessing loop
    while number_of_tries < tries:
        number_of_tries += 1  # Increment tries

        # Get a letter from the player
        while True:
            try:
                user_input = str(input("Guess a letter : " + guessing_result + " -> ").upper())
                if len(user_input) == 1 and user_input.isalpha():  # Ensure the input is a single letter
                    break
                print("Input only letters and 1 letter at a time.")

            except ValueError:
                print("Please input a letter.")

        # Check if the letter has already been guessed
        if user_input in letters_guessed:
            print("You already used that letter! ")
            number_of_tries -= 1  # Deduct a try for duplicate input
            print("Used letters : " + letters_guessed + "\n")

        # If the letter isn't in the word
        elif user_input not in letters_of_the_word:
            letters_guessed += " " + user_input
            print("The word doesn't contain that letter")
            print("Used letters : " + letters_guessed + "\n")

        # If the letter is in the word
        else:
            letters_guessed += " " + user_input
            for index, letter in enumerate(chosen_word):
                if letter == user_input:
                    guessing_result = guessing_result[:index] + user_input + guessing_result[index + 1:]
            print("Good job! " + guessing_result + " (Used letters :" + letters_guessed + ")")

        # Check if the word has been completely guessed
        if "_" not in guessing_result:
            print("Congratulations! You guessed the word.")
            global wins_player
            wins_player += 1  # Increment the player's win count
            break

    # If the player runs out of tries
    if number_of_tries == tries:
        print("You ran out of tries. The word was - ", chosen_word)


# Function for the computer to play the Hangman game
def hangman_comp():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    tries = random.randint(1,100)  # The computer will try a random number of times between 1 and 100
    print(f"I want {tries} tries.")
    letters_guessed = ""  # Store the letters guessed by the computer

    # Find the longest and shortest words in the words list
    longest_word = max(w, key=len)
    longest_length = len(longest_word)

    shortest_word = min(w, key=len)
    shortest_length = len(shortest_word)

    # Ask the player for the number of letters in their word
    while True:
        try:
            number_of_letters = int(input("How many letters does your word have -> "))
            if longest_length >= number_of_letters >= shortest_length:
                break  # Valid number of letters
            print("There isn't a word of that length! Choose another word.")

        except ValueError:
            print("Invalid input!")

    times_tried = 0
    times_repeated = 0
    guessing_result = number_of_letters * "_"

    # The computer starts guessing
    while tries > times_tried:
        times_tried += 1
        letters_left_to_guess = number_of_letters
        comp_letter_input = random.choice(letters).upper()  # Computer picks a random letter
        print("Letters used : " + letters_guessed)

        # If the computer has already guessed the letter
        if comp_letter_input in letters_guessed:
            print("Does your word contain the letter - " + comp_letter_input)
            print("Oops, I already used that letter! \n")
            times_tried -= 1

        elif comp_letter_input not in letters_guessed:

            while True:
                try:
                    user_answer = input(f"\nDoes your word contain the letter {comp_letter_input} (yes/no) -> ")
                    if user_answer == "yes":
                        break
                    elif user_answer == "no":
                        break
                    else:
                        print("Answer with yes/no please.")
                except ValueError:
                    print("Invalid input!")

            # If the letter is in the word
            if user_answer == "yes":
                letters_guessed += " " + comp_letter_input
                while True:
                    try:
                        number_of_repetitions = int(input("How many times -> "))
                        if number_of_repetitions <= letters_left_to_guess:
                            break
                        print("There isn't that many letters left!")
                        break
                    except ValueError:
                        print("Invalid input!")

                # Computer guesses letter positions
                while number_of_repetitions > 0:
                    while True:
                        try:
                            position = int(input("Which positions? -> "))
                            position -= 1
                            if 0 <= position < number_of_letters:
                                if guessing_result[position] == "_":
                                    number_of_repetitions -= 1
                                    guessing_result = guessing_result[:position] + comp_letter_input + guessing_result[position + 1:]
                                    letters_left_to_guess -= 1
                                    print("Result -> ", guessing_result, "\n")
                                    break
                                else:
                                    print("That position is already solved.")
                                break
                            else:
                                print("There isn't that many letters in the word.")
                        except ValueError:
                            print("Invalid input!")

                print("Result -> ", guessing_result)

            # If the letter is not in the word
            elif user_answer == "no":
                letters_guessed += " " + comp_letter_input
                print("Result -> ", guessing_result)
                pass

        # If the computer guesses the word
        if "_" not in guessing_result:
            print("YES! I guessed the right word -> ", guessing_result)
            global wins_comp
            wins_comp += 1

            if guessing_result.lower() not in w:
                print("(even though i'm not sure that word exists :D)")
            break

        # If the computer runs out of tries
        if times_tried + times_repeated == tries:
            print("Dang. I am out of tries.")


# Main game loop
def play():
    while True:
        try:
            print("Press 1 if you want to guess!")
            print("Press 2 if you want me to guess!")
            choose_mode = int(input("-> "))
            if choose_mode in [1, 2]:
                if choose_mode == 1:
                    hangman_player()  # Player guesses the word
                elif choose_mode == 2:
                    hangman_comp()  # Computer guesses the word
                else:
                    print("Please choose 1 or 2!")

        except ValueError:
            print("Invalid input!")

        # Prints the result
        global wins_comp, wins_player
        print(f"\nSCORE\n"
              f"COMP {wins_comp} - {wins_player} PLAYER")

        # Checks if you want to play again
        while True:
            try:
                repeat_game = input("\nDo you want to play again? (yes/no) -> ")
                if repeat_game == "yes":
                    play()  # Restart the game
                elif repeat_game == "no":
                    print("GAME OVER")
                    return  # Exit the game
                else:
                    print("Answer with yes/no please.")
            except ValueError:
                print("Invalid input!")


print_instructions()  # Display the instructions
play()  # Start the game