import random 
r = random.randint(1, 100)
guess = 0
i = 0
while i != r:
    guess += 1
    i = int(input("Enter your Guess: "))
    if(i<r):
        print("Higher")
    elif(i>r):
        print("Lower")
    elif(i==r):
        print(f"YAY! Correct guess: {r}, Number of GUESSES: {guess}")
    else:
        print("Something went wrong!")
    