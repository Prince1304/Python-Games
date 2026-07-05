# 🎨 Color Guessing Game

A simple, interactive console-based color guessing game built with Python. Players can deposit virtual currency, wager their balance to guess the correct color, withdraw their earnings, and track their balance in real-time.

---

## 🚀 Features

* **Virtual Wallet Management:** * **Deposit:** Add funds to your account balance at any time.
    * **Withdraw:** Cash out your winnings (with built-in balance verification to prevent over-withdrawing).
* **Color Betting Gameplay:** * Requires a minimum balance of **10 units** to play.
    * Win rewards (+9 units) on a correct guess.
    * Deducts funds (-10 units) on an incorrect guess.
* **Infinite Game Loop:** The game runs continuously via an interactive menu until the player explicitly chooses to exit.

---

## 🎮 How to Play

1.  **Run the script** using Python.
2.  **Deposit funds** first (Choice `2`), as the game starts with a 0 balance.
3.  **Start the game** (Choice `1`) and try to guess the secret color!
4.  Input your choices using the numeric options provided in the menus.

---

## 🖥️ Sample Output View

Here is an example of how the game looks and functions in the terminal:

```text
-----Start Game-----
1. Start Game
2. Deposit
3. Withdraw
4. Exit
Enter your choice: 2
Your Balance is 0
Enter your Deposit Amount: 20
-----Deposit Successful-----
Your Balance is 20

-----Start Game-----
1. Start Game
2. Deposit
3. Withdraw
4. Exit
Enter your choice: 1
-----Enter Your Color-----
1. red
2. green
3. blue
4. Exit
Enter your choice: 1
Congratulations! You Won! 9
Balance is  29

Enter your choice: 2
Batter Luck Next Time!
Answer Is  Red
Balance is  19

Enter your choice: 4
Come Again
Your Balance is 19

-----Start Game-----
1. Start Game
2. Deposit
3. Withdraw
4. Exit
Enter your choice: 3
Your Balance is 19
Enter your Withdraw Amount: 15
-----Withdrawal Successful-----
Your Balance is 4

-----Start Game-----
1. Start Game
2. Deposit
3. Withdraw
4. Exit
Enter your choice: 4
Game Over
