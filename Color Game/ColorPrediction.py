import random

acc = 0

while True:
    print("-----Start Game-----")
    print("1. Start Game")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    no = int(input("Enter your choice:"))
    if no==1:
        if acc >= 10:
            print("-----Enter Your Color-----")
            print("1. red")
            print("2. green")
            print("3. blue")
            print("4. Exit")
            while True:
                no = input("Enter your choice:")
                com = '1'
                if com == '1':
                    color = "Red"
                elif com == '2':
                    color = "Green"
                else:
                    color = "Blue"
                if no == '4':
                    print("Come Again")
                    print("Your Balance is", acc)
                    break
                elif no == com or no == color:
                    print("Congratulations! You Won! 9")
                    acc = acc + 9
                    print("Balance is ", acc)
                else:
                    print("Batter Luck Next Time!")
                    if com == '1':
                        col = "Red"
                    elif com == '2':
                        col = "Green"
                    else:
                        col = "Blue"
                    print("Answer Is ", col)
                    acc = acc - 10
                    print("Balance is ", acc)
        else:
            print("Your Balance is Not Enough To Play First Deposit Found")
            pass

    elif no==2:
        print("Your Balance is", acc)
        dep= int(input("Enter your Deposit Amount:"))
        acc = acc + dep
        print("-----Deposit Successful-----")
        print("Your Balance is", acc)
    elif no==3:
        print("Your Balance is", acc)
        withd = int(input("Enter your Withdraw Amount:"))
        if withd<=acc:
            acc = acc - withd
            print("-----Withdrawal Successful-----")
        else:
            print("Not enough money Play More!")
        print("Your Balance is", acc)
    elif no==4:
        print("Game Over")
        break
    else:
        print("Wrong Input")

