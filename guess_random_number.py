import random

start=input("Enter starting point: ")
end=input("Enter ending point: ")

num = random.randint(int(start), int(end))
found=False
i=0
while not found:
    i+=1
    guess = input("Enter your guess: ")
    if int(guess) > num:
        print("Too high!")
    elif int(guess) < num:
        print("Too low")
    elif int(guess) == num:
        print(f"You're correct! The number is {num}!")
        print(f"You guessed it in {i} turns!")
        found=True