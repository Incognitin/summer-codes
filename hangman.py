import time
import random

hangman_words = ["cacophony", "cognition", "dissertation", "epiphany", "exponential", "meticulous", "intellectual",
                 "nominal", "crazy", "pneumonoultramicroscopicsilicovolcanoconiosis"]


def hangman():
    print("Let's play hangman!!\n ")
    word_list = list(random.choice(hangman_words))
    length = len(word_list)
    count = 0
    display_list = '_' * length
    guessed = []
    old_len = len(guessed)
    play_game = True
    # print(word_list)
    print(display_list)
    print("This word has {} letters in it\n".format(length))
    while play_game == True:
        Guess = str(input("Enter your guess(Only letters!!)\n"))
        # for letter in word_list:
        # print("")
        for num in range(length):
            if Guess == word_list[num]:
                display_list = display_list[:num] + Guess + display_list[num + 1:]
                guessed.append(Guess)
                time.sleep(1)
                print(display_list)
                # print(word_list)
                # Guess = str(input("Enter your guess(Only letters!!)"))


            elif Guess not in word_list:
                count += 1
                # return(count)
                #Guess = str(input("Enter your guess(Only letters!!)"))

            while word_list == list(display_list) or list(Guess) == word_list:
                play_game = False
                return ("You win!!!!")
            while count == 72:
                play_game = False

                return ("   _____ \n"
                        "  |     | \n"
                        "  |     |\n"
                        "  |     | \n"
                        "  |     O \n"
                        "  |    /|\ \n"
                        "  |    / \ \n"
                        "__|__\n"
                        "Wrong guess. You are hanged!!!\n")
                # return("Wrong guess. You are hanged!!!\n")


print(hangman())