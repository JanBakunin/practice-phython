import random
rand = random.randint(1,9)
guess = 0
count = 0
while guess != "exit" or guess == rand:
    guess = input("Guess a number between 1 and 9: ")
    
    if guess == "exit":
        break
    
    guess = int(guess)
    count += 1
    if guess > rand:
        print("Too high!")
    elif guess < rand:
        print("Too low!")
    else:
        print("Exactly right.")
        print("You guessed", count, "time(s)")
        break
    
