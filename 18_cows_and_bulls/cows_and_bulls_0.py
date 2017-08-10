import random
digits = random.sample(range(10),4)
digits = ''.join(map(str, digits))

def cows_and_bulls():
    guess = "0"
    while guess != digits:
        cows = 0
        bulls = 0
        
        guess = input("Guess a number: ")
        for i in range(0, 4):
            if guess[i] == digits[i]:
                cows += 1
            else:
                bulls += 1
        print(cows, "cow(s) and" ,bulls, "bull(s)")
    print("You win the game the number was " +digits)
cows_and_bulls()