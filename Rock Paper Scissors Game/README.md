# Rock, Paper, Scissors (RPS Game) ✊ ✌️ ✋

An interactive, text-based Rock, Paper, Scissors game built using Python. The application features an AI opponent, automated win/loss verification using deterministic game matrices, live score tracking, and persistent sessions.

## 🌟 Features

* **Interactive Menu System:** Seamlessly navigate between starting a match, viewing performance-based score tiers, resetting your history, or quitting.
* **Smart Verification Logic:** Uses efficient dictionary mapping to evaluate winners instantly without complex nested conditional loops.
* **Robust Input Safety:** Equipped with validation handling to prevent program execution crashes from unexpected or erroneous inputs.
* **Animated Feedback:** Uses standard Unicode emojis to simulate visual gameplay actions directly inside your terminal window.

---

## 🛠️ Game Rules

* **Rock (`1`)** beats **Scissors (`2`)**
* **Scissors (`2`)** beats **Paper (`3`)**
* **Paper (`3`)** beats **Rock (`1`)**
* Each victory awards **100 points**. Ties and losses do not deduct points.


## ⚙️ Prerequisites & Execution
1. Ensure Python 3.x is installed on your computer.
2. Run the application from your terminal or command prompt:
```bash
python RPS.py
```

## 🖥️ Output Preview

```text
**************************************************
               Welcome To The Game                
**************************************************
1. Play The Game
2. View Score
3. New Game
4. Quit
**************************************************
Enter your choice: 1
**************************************************
Press 'q' to return to Main Menu
Please enter your Choice 
1.✊
2.✌️
3.✋
Choice: 1

You chose: ✊
AI chose: ✌️
🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆
Congratulations! You Won!
🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆
**************************************************
Press 'q' to return to Main Menu
Please enter your Choice 
1.✊
2.✌️
3.✋
Choice: q
Returning to Main Menu...
**************************************************
1. Play The Game
2. View Score
3. New Game
4. Quit
**************************************************
Enter your choice: 2
==================================================
Your Score: 100
Play More To Win More!
==================================================
