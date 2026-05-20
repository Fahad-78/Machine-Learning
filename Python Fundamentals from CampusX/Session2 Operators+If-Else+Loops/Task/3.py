#Ask the user to guess a secret number (hardcode it as 7). Keep asking until they guess correctly using a while loop.

import random
num = int(input("Guess the secret number from 1 to 10: "))

rand = random.randint(1,10)

while rand != num:
    num = int(input("Guess again: "))
print("correct!")