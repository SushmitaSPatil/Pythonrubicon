import random
from random import randint


while True:
    while True:
        print(''' Select the level:
            1.Easy
            2.Medium
            3.Hard
        ''')
        end=0
    
        select_level=int(input("Enter your level: "))

        if select_level==1:
            print("You have selected easy level")
            end=30
            break

        elif select_level==2:
            print("You have selected medium level")
            end=60
            break

        elif select_level==3:
            print("You have selected hard level")
            end=100
            break

        else:
            print("Invalid input...Try again")
        
    random_num = randint(1,end)
    
    print(random_num)
    attempts=3
    while True:
        user_num=int(input(f"Enter the number between 1 to {end}: "))
        if random_num == user_num:
            print("You guessed right number")
            play_again = input("Do you want to play again? (y/n): ")
            if play_again == 'y':
                print("Restarting game...")
                break
            else:
                print("Quitting game")
                exit()
        elif attempts == 1:
            print(f"You loose...the number is {random_num}")
            exit()
        else:
            attempts -=1
            print(f"Incorrect Number...you have {attempts} attempts left") 
            

