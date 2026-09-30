# 📘 Assignment: Games in Python

## 🎯 Objective

Create a simple text-based game in Python that uses loops, conditionals, user input, and string manipulation to make a fun interactive experience.

## 📝 Tasks

### 🛠️ Hangman Game Setup

#### Description
Create a Python program that selects a random word from a list and displays a masked version for the player to guess.

#### Requirements
Completed program should:

- Store a list of words for the game.
- Randomly choose one word at the start of the game.
- Show the hidden word as underscores, such as `_ _ _ _`.
- Allow the player to enter one letter at a time.
- Reveal matching letters in their correct positions.
- Example output:
```python
Word: _ _ _ _ _
Guess a letter: a
Word: a _ _ _ a
```

### 🛠️ Game Loop and Win/Lose Logic

#### Description
Add the gameplay loop that tracks incorrect guesses, checks for wins and losses, and ends the game with a clear result.

#### Requirements
Completed program should:

- Give the player a limited number of wrong guesses.
- Track guessed letters so the player cannot repeat them.
- Display remaining attempts after each guess.
- End the game when the player successfully guesses the word or runs out of attempts.
- Print a final message such as:
```python
You win! The word was "python"
```
or
```python
Game over! The word was "python"
```
