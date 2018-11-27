import random

num = random.randint(0,128)
print("guess a number between 1 and 127>")

guess = int(input())
while(guess != num):
    print("incorrect")
    if(guess < num):
        print("higher")
    else:
        print("lower")
    print("guess a number >")
    guess = int(input())

print("correct! guess: " + str(guess) + " is the number: " + str(num))
