# 🎮 Python Number Guessing Game

A clean, robust, and interactive number guessing game written in Python. The computer picks a secret number between 1 and 10, and you have 5 attempts to guess it right with smart hints along the way!

---

## ✨ Features
* **Suspenseful Pauses:** Uses `time.sleep` to build excitement before revealing if you won.
* **Smart Hints:** Tells you whether to guess higher or lower after an incorrect choice.
* **Crash Protection:** Safely handles cases where a user accidentally types text (e.g., "three") instead of a digit.
* **Polished Mechanics:** Uses a `while` loop to accurately track remaining attempts.

---

## 🖥️ How it Looks (Output View)

### Winning Scenario:
```text
Welcome to the Guessing Game! I'm thinking of a number between 1 and 10.

Enter your guess: 5
Wrong! 4 attempts left.
💡 Try a higher number.

Enter your guess: 8
Wrong! 3 attempts left.
💡 Try a lower number.

Enter your guess: 7

Hmm... what do you think? Are you right? 🤔
*(3-second pause)*
Yes, of course! Congratulations! You guessed the right number! 🎉
```
