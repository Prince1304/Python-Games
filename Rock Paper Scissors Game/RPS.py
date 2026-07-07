import random

class Game:
    score = 0
    def __init__(self):
        print("*" * 50)
        print("Welcome To The Game")
        print("*" * 50)
        while True:
            print("1. Play The Game")
            print("2. View Score")
            print("3. New Game")
            print("4. Quit")
            print("*" * 50)
            choice = int(input("Enter your choice: "))
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
        while True:
            Ai = random.choice('123')
            Ai_res =''
            if Ai == 1:
                Ai_res ='✊'
            elif Ai == 2:
                Ai_res ='✌️'
            elif Ai == 3:
                Ai_res = '✋'
            user = ''
            print("*" * 50)
            choice = str(input("Please enter your Choice \n1.✊\n2.✌️\n3.✋\n): "))
            user_res = ''
            if choice == "1":
                user = '1'
                user_res = '✊'
            elif choice == "2":
                user = '️2️'
                user_res = '✌️'
            elif choice == "3":
                user = '️3'
                user_res = '✋'
            elif choice == "q":
                user = 'q'
            print("Press q to Quit")
            if user == 'q':
                print("Game Over!")
                break
            pattern = [Ai, user]
            win = [['1', '3'], ['2', '1'], ['3', '2']]
            print(pattern)
            if Ai == user:
                print("=" * 50)
                print("Match Tie!")
                print("=" * 50)
            elif pattern not in win:
                print("🏆"*15)
                print(f"Ai Choose : {Ai_res}")
                print("Congratulations! You Won!")
                print("🏆" * 15)
                self.score += 100
            else:
                print("*" * 50)
                print("Opp's! You Lose!")
                print(f"The Ai Choose {Ai_res}")
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
        elif self.score > 500:
            print("Wow! you Won 5+ Games!")
            print(f"Your Score: {self.score}")
        elif self.score >= 1000:
            print("Wow! you Won 10 Games!")
            print(f"Your Score: {self.score}")
        elif self.score > 1000:
            print("Wow! you Won 10+ Games!")
            print(f"Your Score: {self.score}")
        print("=" * 50)

    def newgame(self):
        self.score = 0
        print("New Game Started!")
        self.play()

game = Game()
