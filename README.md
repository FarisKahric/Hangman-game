# Hangman Game

## Description

This is a Python implementation of the classic Hangman game. The game allows users to either guess a randomly selected word or let the computer attempt to guess a word chosen by the user. The game includes error handling, user input validation, and customizable difficulty levels.

## Features

- **Single-player mode**: The player guesses letters to reveal the hidden word.
- **Computer-guess mode**: The player thinks of a word, and the computer attempts to guess it.
- **Random word selection**: Words are chosen randomly from an external text file.
- **Custom number of attempts**: Players can specify how many tries they want.
- **Tracking guessed letters**: The game keeps track of used letters to avoid repetition.
- **Dynamic display of guessed progress**: The word updates as correct letters are guessed.

## Installation

To run the Hangman game, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/FarisKahric/Hangman-Game.git
   cd Hangman-Game
   ```

2. **Ensure you have Python installed** (Python 3.x recommended). If not, download it from [Python's official website](https://www.python.org/).

3. **Install dependencies** (if needed):

   ```bash
   pip install -r requirements.txt
   ```

   *(Note: The game primarily uses built-in Python libraries, so this step may not be necessary.)*

## How to Play

Run the script by executing:

```bash
python hangman.py
```

### Player Mode (You guess the word)

1. Choose how many attempts you want.
2. Enter one letter at a time to guess the hidden word.
3. If the letter is correct, it will be revealed in the word.
4. If incorrect, the number of attempts left decreases.
5. Win by guessing all letters before running out of attempts.

### Computer Mode (The computer guesses your word)

1. The computer randomly selects letters and asks if they are in your word.
2. If correct, you must input how many times it appears and its position(s).
3. The game continues until the computer correctly guesses the full word or runs out of attempts.

## File Structure

```
Hangman-Game/
│── hangman.py          # Main game script
│── words.txt           # Text file containing word list
│── README.md           # This documentation
│── requirements.txt    # Dependencies (if needed)
```


## License

This project is open-source and available under the **MIT License**.

## Contributions

Contributions are welcome! Feel free to fork the repository, create a feature branch, and submit a pull request.

## Contact

If you have any questions or suggestions, reach out to me via [GitHub Issues](https://github.com/FarisKahric/Hangman-Game/issues).

