#Guessing Game

import random
jackpot = random.randint(1,100)

guess = int(input('Guess any number between 1 to 100: '))

count = 1
while guess!=jackpot:
    if guess<jackpot:
        print('Wrong, guess higher')
    else:
        print('Wrong, guess lower')

    guess = int(input('Guess any number between 1 to 100: '))
    count += 1

else:
    print('Correct guess')
    print('Attempts: ',count)