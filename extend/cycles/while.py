import random

random_num = random.randint(1, 5)

while True:
    guess = int(input("Enter a guess: "))
    if guess == random_num:
        print("You guessed the number!")
        break
    else:
        print("Try again!")
        continue