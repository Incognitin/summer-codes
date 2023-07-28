import random

# all lists
alphabets = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['-','+','[',']','|','/','<','>','?','*','&','^','%','$','#','@','!','=']

#all random generators
alphashuffle = random.randint(0,25)
digitshuffle = random.randint(0,9)
symbolshuffle = random.randint(0,17)

password = []

#Two upper case letters

Upper = alphabets[alphashuffle].upper()
password.append(Upper)
alphashuffle = random.randint(0,25)
Uppertwo = alphabets[alphashuffle].upper()
password.append(Uppertwo)

#Two lower case letters

alphashuffle = random.randint(0,25)
password.append(alphabets[alphashuffle])
alphashuffle = random.randint(0,25)
password.append(alphabets[alphashuffle])

#Two digits

password.append(numbers[digitshuffle])
digitshuffle = random.randint(0,9)
password.append(numbers[digitshuffle])

#Two symbols
password.append(symbols[symbolshuffle])
symbolshuffle = random.randint(0,17)
password.append(symbols[symbolshuffle])

random.shuffle(password)


def listToString(password):
        
    final = ""
    for ind in password:
        final += ind

    return final

print(listToString(password))






