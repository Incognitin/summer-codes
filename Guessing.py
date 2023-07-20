import random

comp = random.randint(0,10)
play_game = True
while play_game == True:
    player = int(input("guess your number: "))
    if player == comp:
        print("You win!")
        play_game == False
        break
    else:
        if player > comp:
            print("The number should be lower ")
        elif player < comp:
            print("The number should be higher ")

