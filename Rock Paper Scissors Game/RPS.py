import random

class Game:
    score = 0

    def __init__(self):
        print("*" * 50)
        print(f"{'Welcome To The Game':^50}")
        print("*" * 50)
        while True:
            print("1. Play The Game")
            print("2. View Score")
            print("3. New Game")
            print("4. Quit")
            print("*" * 50)
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == 1:
                self.play()
            elif choice == 2:
                self.scores()
            elif choice == 3:
                self.newgame()
            elif choice == 4:
                print("=" * 100)
                print("Thank You For Playing The Game, Come Again and Make Big Score!")
                print("=" * 100)
                break

    def play(self):
        # Dictionary mapping for cleaner conversion
        moves = {'1': '✊', '2': '✌️', '3': '✋'}
        
        # Rules: win[player_move] = what_it_beats
        win_rules = {'1': '2', '2': '3', '3': '1'}

        while True:
            print("*" * 50)
            print("Press 'q' to return to Main Menu")
            user = input("Please enter your Choice \n1.✊\n2.✌️\n3.✋\nChoice: ").strip().lower()

            if user == 'q':
                print("Returning to Main Menu...")
                break
            
            if user not in ['1', '2', '3']:
                print("Invalid choice! Please select 1, 2, 3, or q.")
                continue

            # Secure clean AI choices matching the user data type (strings)
            ai = random.choice(['1', '2', '3'])

            print(f"\nYou chose: {moves[user]}")
            print(f"AI chose: {moves[ai]}")

            if user == ai:
                print("=" * 50)
                print("Match Tie!")
                print("=" * 50)
            elif win_rules[user] == ai:
                print("🏆" * 15)
                print("Congratulations! You Won!")
                print("🏆" * 15)
                self.score += 100
            else:
                print("*" * 50)
                print("Oops! You Lose!")
                print("*" * 50)

    def scores(self):
        print("=" * 50)
        if self.score == 0:
            print("Please Play The Game First!")
        elif self.score < 500:
            print(f"Your Score: {self.score}")
            print("Play More To Win More!")
        elif self.score == 500:
            print("Wow! you Won 5 Games!")
            print(f"Your Score: {self.score}")
        elif 500 < self.score < 1000:
            print("Wow! you Won 5+ Games!")
            print(f"Your Score: {self.score}")
        elif self.score == 1000:
            print("Wow! you Won 10 Games!")
            print(f"Your Score: {self.score}")
        else:  # score > 1000
            print("Wow! you Won 10+ Games!")
            print(f"Your Score: {self.score}")
        print("=" * 50)

    def newgame(self):
        self.score = 0
        print("\nNew Game Started! Score reset to 0.")
        self.play()

if __name__ == "__main__":
    game = Game()
