import random
import time

# all lists
alphabets = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#Dict = {'a': '!', 'b': 'For', 'a': }
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['-','+','[',']','|','/','<','>','?','*','&','^','%','$','#','@','!','=']

#all random generators
alphacheck = random.randint(0,25)
digitcheck = random.randint(0,9)
symbolcheck = random.randint(0,17)

# encode loops
user = input(" Enter a word or sentence to encode ")
mega_user = list(user)
length = len(mega_user)
final_string = ""
for x in range(0,int(length)):
    # forming variable to individually add each variable

    alphacheck = random.randint(0, 25)
    symbolcheck = random.randint(0, 17)
    numbercheck = random.randint(0,9)
    letter = alphabets[alphacheck]
    symbol = symbols[symbolcheck]
    number = numbers[numbercheck]
    if mega_user[x] == " ":
        final_string += " "

    finder = random.randint(1,4)
    for y in range(0,4, finder):
        if y == 1:
            final_string += letter
        elif y == 2:
            final_string += symbol
        elif y == 3:
            final_string += number





print("Your message has been successfully encoded: {}".format(final_string))
time.sleep(3)




