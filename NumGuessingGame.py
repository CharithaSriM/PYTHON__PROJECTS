#importing random module
import random
num = random.randrange(1,100)
guess = int(input("Enter any number: "))
while num!= guess:
    if guess < num:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > num:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
        break
print("Yea ! You guessed it right!!")