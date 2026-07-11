import random
import time

secret_number = random.randint(1, 10)
attempts_left = 5  

print("Welcome to the Guessing Game! I'm thinking of a number between 1 and 10.")

while attempts_left > 0:
    try:
        user_guess = int(input("\nEnter your guess: "))
    except ValueError:
        print("Oops! Please enter a valid whole number.")
        continue

    if user_guess == secret_number:
        print("\nHmm... what do you think? Are you right? 🤔")
        time.sleep(3) 
        print("Yes, of course! Congratulations! You guessed the right number! 🎉")
        break
    else:
        attempts_left -= 1
        
        if attempts_left > 0:
            print(f"Wrong! {attempts_left} attempts left.")
            if user_guess > secret_number:
                print("💡 Try a lower number.")
            else:
                print("💡 Try a higher number.")
        else:
            print(f"\nGame Over! Don't be upset, you'll get it next time. The number was {secret_number}.")
